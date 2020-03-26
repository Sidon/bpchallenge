from django.views.generic import TemplateView


# Front
class ReadMeView(TemplateView):
    template_name = "bpchallenge/home.html"

    def get_context_data(self, **kwargs):
        rst_file = kwargs['rst_file']
        with open(rst_file, 'r') as f:
            text = f.read()

        print(kwargs)

        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['text'] = text

        return context

