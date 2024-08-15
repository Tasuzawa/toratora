from django_components import Component, register

@register("favicon")
class Favicon(Component):
    template_name = "favicon/template.html"

#    def get_context_data(self, value):
#        return {
#            "param": "sample value",
#        }

#    class Media:
#        css = "favicon/style.css"
#        js = "favicon/script.js"