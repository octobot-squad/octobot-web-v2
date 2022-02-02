from home.models import Team, Portfolio, Total


def total(request):
    total_latest = Total.objects.all().order_by('-id')[:1]
    context = {
        'total_latest': total_latest,
    }
    return context


def teamview(request):
    team_latest = Team.objects.all().order_by('-id')[:25]
    context = {
        'team_latest': team_latest,
    }
    return context


def portfolioview(request):
    portfolio_latest = Portfolio.objects.all().order_by('-id')[:25]
    context = {
        'portfolio_latest': portfolio_latest,
    }
    return context
