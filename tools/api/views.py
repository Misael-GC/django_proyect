from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.renderers import BaseRenderer
from xhtml2pdf import pisa
from tools.models import Tool
from .serializers import ToolSerializer

class PDFRenderer(BaseRenderer):
    media_type = 'application/pdf'
    format = 'pdf'
    charset = None
    render_style = 'binary'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        return data

class ToolViewSet(viewsets.ModelViewSet):
    queryset = Tool.objects.all()
    serializer_class = ToolSerializer

    @action(detail=False, methods=['get'], url_path='pdf', renderer_classes=[PDFRenderer])
    def reporte_pdf(self, request):
        # Obtener todas las herramientas del modelo Tool
        tools = Tool.objects.all().order_by('name')
        
        # Cargar y renderizar la plantilla HTML con el contexto
        template = get_template('reporte_herramientas.html')
        context = {
            'herramientas': tools,
        }
        html = template.render(context)
        
        # Convertir HTML a PDF usando xhtml2pdf
        result = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("utf-8")), result)
        
        if not pdf.err:
            response = HttpResponse(result.getvalue(), content_type='application/pdf')
            # Retorna el archivo inline para visualización, o attachment para descarga
            response['Content-Disposition'] = 'inline; filename="Herramientas_MarketTrack.pdf"'
            return response
            
        return HttpResponse("Error al generar el archivo PDF", status=500)