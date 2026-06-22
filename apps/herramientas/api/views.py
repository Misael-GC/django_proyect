from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.renderers import BaseRenderer
from xhtml2pdf import pisa
from ..models import Herramienta
from .serializers import HerramientaSerializer

class PDFRenderer(BaseRenderer):
    media_type = 'application/pdf'
    format = 'pdf'
    charset = None
    render_style = 'binary'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        return data

class HerramientaViewSet(viewsets.ModelViewSet):
    queryset = Herramienta.objects.all()
    serializer_class = HerramientaSerializer

    @action(detail=False, methods=['get'], url_path='pdf', renderer_classes=[PDFRenderer])
    def reporte_pdf(self, request):
        # Obtener todas las herramientas
        herramientas = Herramienta.objects.all().order_by('nombre')
        
        # Cargar y renderizar la plantilla HTML con el contexto
        template = get_template('reporte_herramientas.html')
        context = {
            'herramientas': herramientas,
        }
        html = template.render(context)
        
        # Convertir HTML a PDF usando xhtml2pdf
        result = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("utf-8")), result)
        
        if not pdf.err:
            response = HttpResponse(result.getvalue(), content_type='application/pdf')
            # Usar 'inline' permite abrir en el navegador, o 'attachment' para forzar descarga
            response['Content-Disposition'] = 'inline; filename="reporte_herramientas.pdf"'
            return response
            
        return HttpResponse("Error al generar el archivo PDF", status=500)