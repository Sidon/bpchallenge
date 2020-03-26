from django.conf import settings
from django.utils.translation import npgettext_lazy, pgettext_lazy
from enum import Enum


class OrderStatus:
    DRAFT = 'draft'
    UNFULFILLED = 'unfulfilled'
    PARTIALLY_FULFILLED = 'partially fulfilled'
    FULFILLED = 'fulfilled'
    CANCELED = 'canceled'

    CHOICES = [
        (DRAFT, pgettext_lazy(
            'Status for a fully editable, not confirmed order created by '
            'staff users',
            'Draft')),
        (UNFULFILLED, pgettext_lazy(
            'Status for an order with no items marked as fulfilled',
            'Unfulfilled')),
        (PARTIALLY_FULFILLED, pgettext_lazy(
            'Status for an order with some items marked as fulfilled',
            'Partially fulfilled')),
        (FULFILLED, pgettext_lazy(
            'Status for an order with all items marked as fulfilled',
            'Fulfilled')),
        (CANCELED, pgettext_lazy(
            'Status for a permanently canceled order',
            'Canceled'))]


class OrderEvents(Enum):
    PLACED = 'placed'
    PLACED_FROM_DRAFT = 'draft_placed'
    OVERSOLD_ITEMS = 'oversold_items'
    ORDER_MARKED_AS_PAID = 'marked_as_paid'
    CANCELED = 'canceled'
    ORDER_FULLY_PAID = 'order_paid'
    UPDATED = 'updated'

    EMAIL_SENT = 'email_sent'

    PAYMENT_CAPTURED = 'captured'
    PAYMENT_REFUNDED = 'refunded'
    PAYMENT_VOIDED = 'voided'

    FULFILLMENT_CANCELED = 'fulfillment_canceled'
    FULFILLMENT_RESTOCKED_ITEMS = 'restocked_items'
    FULFILLMENT_FULFILLED_ITEMS = 'fulfilled_items'
    TRACKING_UPDATED = 'tracking_updated'
    NOTE_ADDED = 'note_added'

    # Used mostly for importing legacy data from before Enum-based events
    OTHER = 'other'


class OrderEventsEmails(Enum):
    PAYMENT = 'payment_confirmation'
    SHIPPING = 'shipping_confirmation'
    ORDER = 'order_confirmation'
    FULFILLMENT = 'fulfillment_confirmation'


EMAIL_CHOICES = {
    OrderEventsEmails.PAYMENT.value: pgettext_lazy(
        'Email type', 'Payment confirmation'),
    OrderEventsEmails.SHIPPING.value: pgettext_lazy(
        'Email type', 'Shipping confirmation'),
    OrderEventsEmails.FULFILLMENT.value: pgettext_lazy(
        'Email type', 'Fulfillment confirmation'),
    OrderEventsEmails.ORDER.value: pgettext_lazy(
        'Email type', 'Order confirmation')}
