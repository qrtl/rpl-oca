This module adds a field on the Sales & Purchases tab of the partner form where
you can register the default incoterms for new sales orders for this customer.

The field is only visible for customers (company partners and contacts) and user
which have appropriate group 'Display incoterms on Sales Order and related
invoices'. A different incoterm can be set per contact within the same company.

When the customer or the delivery address is selected on a new quotation, the incoterm
is retrieved from either of the partner record based on the following logic:

* Take the incoterm of the delivery address if it has one set.
* Otherwise, take the incoterm of the customer if it has one set.
