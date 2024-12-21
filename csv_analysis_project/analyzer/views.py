from django.shortcuts import render
from .forms import CSVUploadForm
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def upload_and_analyze(request):
    context = {}

    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            file_path = f'temp_{uploaded_file.name}'
            with open(file_path, 'wb+') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)

            try:
                # Read and analyze the CSV file
                data = pd.read_csv(file_path)

                # Add data insights to context
                context['head'] = data.head().to_html()
                context['description'] = data.describe().to_html()
                context['missing'] = data.isnull().sum().to_html()

                # Create a histogram
                plt.figure(figsize=(6, 4))
                sns.histplot(data.select_dtypes(include='number'), kde=True)
                plt.title('Histogram of Numerical Columns')
                hist_image_path = 'static/histogram.png'
                plt.savefig(hist_image_path)
                context['hist_image'] = hist_image_path

                # Clean up temporary file
                os.remove(file_path)

            except Exception as e:
                context['error'] = f"Error reading the file: {e}"

    else:
        form = CSVUploadForm()

    context['form'] = form
    return render(request, 'analyzer/upload.html', context)

