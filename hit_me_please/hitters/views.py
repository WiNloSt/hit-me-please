from django.http import HttpResponse
from django.views import View


class LandingPageView(View):
    def get(self, request):

        html = '''
            <form action="" method="post">
                <label for="email">Email:</label>
                <input id="email" name="email" type="email" />
                <button type="submit">Submit</button>
            </form>
        '''

        return HttpResponse(html)
