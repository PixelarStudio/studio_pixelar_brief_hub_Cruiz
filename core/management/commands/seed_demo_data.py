# core/management/commands/seed_demo_data.py

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils import timezone

from briefs.models import Brief
from accounts.models import Profile
from messaging.models import Message


class Command(BaseCommand):
    help = "Crea datos de demostración (usuario demo, briefs y mensajes)."

    def handle(self, *args, **options):
        self.stdout.write(self.style.MIGRATE_HEADING("Creando datos demo..."))

        # 1) Usuario demo
        demo_username = "demo_user"
        demo_email = "demo@studiopixelar.com"
        demo_password = "Demo1234!"

        demo_user, created = User.objects.get_or_create(
            username=demo_username,
            defaults={"email": demo_email},
        )

        if created:
            demo_user.set_password(demo_password)
            demo_user.first_name = "Demo"
            demo_user.last_name = "Pixelar"
            demo_user.save()
            self.stdout.write(
                self.style.SUCCESS(
                    f"Usuario demo creado: {demo_username}/{demo_password}"
                )
            )
        else:
            self.stdout.write(
                self.style.WARNING(
                    "Usuario demo ya existía; no se modificó la contraseña."
                )
            )

        # 2) Perfil demo
        Profile.objects.get_or_create(
            user=demo_user,
            defaults={
                "bio": "Perfil demo para probar Pixelar Brief Hub.",
                "website": "https://studiopixelar.com",
            },
        )

        # 3) Otro usuario para mensajes
        reviewer_username = "reviewer"
        reviewer_user, reviewer_created = User.objects.get_or_create(
            username=reviewer_username,
            defaults={
                "email": "reviewer@example.com",
                "first_name": "Code",
                "last_name": "Reviewer",
            },
        )
        if reviewer_created:
            reviewer_user.set_password("Reviewer123!")
            reviewer_user.save()
            Profile.objects.get_or_create(
                user=reviewer_user,
                defaults={
                    "bio": "Revisor de proyectos.",
                    "website": "https://example.com",
                },
            )

        # 4) Briefs basados en proyectos reales de Studio Pixelar
        briefs_data = [
            {
                "title": "San Isidro Policlínica Privada",
                "client_name": "San Isidro Policlínica Privada",
                "service_type": "Web corporativa para centro de salud",
                "body": """
<p>Sitio web institucional para San Isidro Policlínica Privada pensado como
punto de entrada único para pacientes y equipo médico. Incluye secciones de
especialidades, profesionales, equipamiento y contacto.</p>
<p>En el proyecto real se implementó con tecnologías modernas orientadas a
componentes, pero en este panel lo usamos como brief de referencia para
documentar contenidos, estructura y flujos de turnos de una web corporativa
de salud.</p>
<p>El foco está en mobile-first, formularios claros, acceso rápido a WhatsApp
y mapa embebido para llegar a la clínica, junto con buenas prácticas de SEO
y rendimiento.</p>
""",
            },
            {
                "title": "Studio Pixelar – Sitio principal",
                "client_name": "Studio Pixelar",
                "service_type": "Diseño y desarrollo web",
                "body": """
<p>Web principal de Studio Pixelar donde se presentan servicios, planes,
portfolio y vías de contacto para emprendedores, marcas personales y PyMEs.</p>
<p>Incluye un cotizador guiado en varios pasos que ayuda a estimar el proyecto
y enviar un resumen por WhatsApp o email. El brief describe las secciones
clave, el flujo del cotizador y cómo se transforman visitas en consultas
reales.</p>
<p>Se prioriza un diseño limpio, mensajes claros y rendimiento, para que la
experiencia sea rápida y entendible desde cualquier dispositivo.</p>
""",
            },
            {
                "title": "Ruba Tecno – E-commerce",
                "client_name": "Ruba Tecno",
                "service_type": "E-commerce",
                "body": """
<p>Tienda online para Ruba Tecno, orientada a la venta organizada del catálogo
de productos de la marca.</p>
<p>En este brief se definen las categorías, fichas de producto y búsquedas,
junto con un checkout confiable basado en WooCommerce. El objetivo es que el
cliente pueda administrar contenidos y promociones sin depender del
desarrollador.</p>
<p>El diseño parte de maquetación visual con Elementor, cuidando jerarquía,
legibilidad y adaptación a móviles para acompañar campañas de tráfico pago y
orgánico.</p>
""",
            },
            {
                "title": "Sempre A Full – E-commerce multilenguaje",
                "client_name": "Sempre A Full",
                "service_type": "E-commerce multilenguaje",
                "body": """
<p>Sempre A Full es una tienda online enfocada en productos EvergreenLife,
con clientes en varios países y necesidad de operar en más de un idioma.</p>
<p>El proyecto real se construyó sobre WordPress y WooCommerce con soporte
multilenguaje y distintas pasarelas de pago. En este brief se documentan
requisitos de catálogo, variaciones, traducciones y contenido educativo
sobre salud y bienestar.</p>
<p>También se registra la importancia del área de cliente, el historial de
compras y la integración con proveedores para mantener stock y precios
actualizados.</p>
""",
            },
        ]

        created_count = 0
        for data in briefs_data:
            brief, created_brief = Brief.objects.get_or_create(
                title=data["title"],
                client_name=data["client_name"],
                defaults={
                    "service_type": data["service_type"],
                    "body": data["body"],
                    "owner": demo_user,
                    "created_at": timezone.now(),
                },
            )
            if created_brief:
                created_count += 1

        self.stdout.write(
            self.style.SUCCESS(f"Briefs demo creados/nuevos: {created_count}")
        )

        # 5) Mensajes demo
        if not Message.objects.filter(sender=demo_user).exists():
            Message.objects.create(
                sender=demo_user,
                recipient=reviewer_user,
                subject="Consulta sobre brief de San Isidro",
                body=(
                    "Hola, ¿qué te parece la estructura del brief para la web de "
                    "San Isidro Policlínica Privada? ¿Ves algo para mejorar?"
                ),
            )
            Message.objects.create(
                sender=reviewer_user,
                recipient=demo_user,
                subject="Feedback sobre briefs de portfolio",
                body=(
                    "Los briefs de San Isidro, Studio Pixelar y los e-commerce "
                    "están claros. Después podemos sumar métricas o anexos si lo necesitás."
                ),
            )
            self.stdout.write(self.style.SUCCESS("Mensajes demo creados."))
        else:
            self.stdout.write(
                self.style.WARNING(
                    "Ya existían mensajes de demo; no se duplicaron."
                )
            )

        self.stdout.write(self.style.SUCCESS("Datos demo listos."))
