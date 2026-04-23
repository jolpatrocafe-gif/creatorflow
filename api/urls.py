from django.urls import path
from .views import (
    generate_review,
    paddle_webhook,
    confirm_plan,
    health,
    finalize_checkout,
    refresh_credits,
    select_basic,
)

urlpatterns = [
    path("generate-review/", generate_review, name="generate_review"),
    path("paddle-webhook/", paddle_webhook, name="paddle_webhook"),
    path("confirm-plan/", confirm_plan, name="confirm_plan"),
    path("health/", health, name="health"),
    path("finalize-checkout/", finalize_checkout, name="finalize_checkout"),
    path("refresh-credits/", refresh_credits, name="refresh_credits"),
    path("select-basic/", select_basic, name="select_basic"),
]
