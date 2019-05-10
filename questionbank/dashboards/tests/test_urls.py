from django.urls import reverse, resolve


def test_dashboard():
    assert reverse('dashboards:dashboard') == '/'
    assert resolve('/').view_name == 'dashboards:dashboard'
