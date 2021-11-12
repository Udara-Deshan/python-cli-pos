# ORDER

### Order properties

```python
class Order:
    def __init__(self, order_id, customer_id, total_price):
        self.order_id = order_id
        self.customer_id = customer_id
        self.total_price = total_price


class OrderDetails:
    def __init__(self, details_id,order_id, item_id, item_qty, item_price):
        self.details_id = details_id
        self.order_id = order_id
        self.item_id = item_id
        self.item_qty = item_qty
        self.item_price = item_price
```

### Order create

```cmd
item create 
```

### Order find by id

```cmd
item find <id>
```

### Order find all

```cmd
item find all
```

### Order search

```cmd
item search <key> <value>
```