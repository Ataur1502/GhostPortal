import os
from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import FileResponse, Http404, HttpResponse
from django.conf import settings

class LandingView(TemplateView):
    template_name = 'portal/landing.html'

    def get(self, request, *args, **kwargs):
        # Redirect authenticated users to the dashboard
        if request.user.is_authenticated:
            from django.shortcuts import redirect
            return redirect('dashboard')
        return super().get(request, *args, **kwargs)

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'portal/dashboard.html'

class DownloadHandbookView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        pdf_path = os.path.join(settings.BASE_DIR, 'portal', 'secure_files', 'Employee_Handbook.pdf')
        if not os.path.exists(pdf_path):
            raise Http404("Handbook file not found.")
        
        response = FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="Employee_Handbook_Final.pdf"'
        return response

def custom_404(request, exception=None):
    return render(request, '404.html', status=404)

def custom_500(request):
    return render(request, '500.html', status=500)
from django.http import HttpResponse


def internal_backup(request):
    flag = "BSCTF{mult1_d0m41n_ch41n_c0mpl3t3}"

    return HttpResponse(
        f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Internal Backup</title>
            <style>
                body {{
                    background: #111827;
                    color: #e5e7eb;
                    font-family: monospace;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                }}

                .card {{
                    background: #1f2937;
                    padding: 40px;
                    border-radius: 12px;
                    border: 1px solid #374151;
                    width: 700px;
                }}

                h2 {{
                    color: #22c55e;
                }}

                pre {{
                    background: #0f172a;
                    padding: 20px;
                    border-radius: 8px;
                    overflow-x: auto;
                }}
            </style>
        </head>
        <body>
            <div class="card">
                <h2>Developer Backup Service</h2>

                <p>Archive Status : OK</p>
                <p>Environment : Production</p>

                <pre>{flag}</pre>

                <p style="opacity:.6;">
                    Internal Development Endpoint
                </p>
            </div>
        </body>
        </html>
        """,
        content_type="text/html",
    )
