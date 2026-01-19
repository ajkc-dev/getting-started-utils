import unittest
from unittest.mock import Mock, MagicMock
from order_system import Order, InventoryService, PaymentGateway, InventoryShortageError, PaymentFailedError, InvalidOrderError

class TestOrderSystem(unittest.TestCase):
    def setUp(self):
        self.mock_inventory = Mock(spec=InventoryService)
        self.mock_payment = Mock(spec=PaymentGateway)
        self.email = "test@example.com"
        self.order = Order(self.mock_inventory, self.mock_payment, self.email)

    def test_initialization(self):
        self.assertEqual(self.order.customer_email, self.email)
        self.assertFalse(self.order.is_vip)
        self.assertEqual(self.order.items, {})
        self.assertFalse(self.order.is_paid)
        self.assertEqual(self.order.status, "DRAFT")

    def test_add_item_valid(self):
        self.order.add_item("item1", 10.0, 2)
        self.assertEqual(self.order.items["item1"], {'price': 10.0, 'qty': 2})
        
        # Add to existing
        self.order.add_item("item1", 10.0, 1)
        self.assertEqual(self.order.items["item1"]['qty'], 3)

    def test_add_item_invalid(self):
        with self.assertRaises(ValueError):
            self.order.add_item("item1", -10.0)
        with self.assertRaises(ValueError):
            self.order.add_item("item1", 10.0, 0)

    def test_remove_item(self):
        self.order.add_item("item1", 10.0)
        self.order.remove_item("item1")
        self.assertNotIn("item1", self.order.items)
        # Removing non-existent shouldn't fail
        self.order.remove_item("item2")

    def test_total_price(self):
        self.order.add_item("p1", 10.0, 2) # 20
        self.order.add_item("p2", 20.0, 1) # 20
        self.assertEqual(self.order.total_price, 40.0)

    def test_apply_discount_vip(self):
        vip_order = Order(self.mock_inventory, self.mock_payment, "vip@example.com", is_vip=True)
        vip_order.add_item("p1", 100.0)
        # 20% off 100 = 80
        self.assertEqual(vip_order.apply_discount(), 80.0)

    def test_apply_discount_bulk(self):
        self.order.add_item("p1", 110.0)
        # 10% off > 100 = 99.0
        self.assertEqual(self.order.apply_discount(), 99.0)

    def test_no_discount(self):
        self.order.add_item("p1", 50.0)
        self.assertEqual(self.order.apply_discount(), 50.0)
    
    def test_checkout_empty(self):
        with self.assertRaises(InvalidOrderError):
            self.order.checkout()

    def test_checkout_success(self):
        self.order.add_item("p1", 50.0)
        self.mock_inventory.get_stock.return_value = 10
        self.mock_payment.charge.return_value = True

        result = self.order.checkout()

        self.mock_inventory.get_stock.assert_called_with("p1")
        self.mock_payment.charge.assert_called_with(50.0, "USD")
        self.mock_inventory.decrement_stock.assert_called_with("p1", 1)
        self.assertTrue(self.order.is_paid)
        self.assertEqual(self.order.status, "COMPLETED")
        self.assertEqual(result["status"], "success")

    def test_checkout_inventory_shortage(self):
        self.order.add_item("p1", 50.0, 5)
        self.mock_inventory.get_stock.return_value = 2 # Less than 5

        with self.assertRaises(InventoryShortageError):
            self.order.checkout()
        
        self.mock_payment.charge.assert_not_called()

    def test_checkout_payment_failure(self):
        self.order.add_item("p1", 50.0)
        self.mock_inventory.get_stock.return_value = 10
        self.mock_payment.charge.return_value = False

        with self.assertRaises(PaymentFailedError):
            self.order.checkout()
            
        self.mock_inventory.decrement_stock.assert_not_called()
        self.assertFalse(self.order.is_paid)

    def test_checkout_payment_error_exception(self):
        self.order.add_item("p1", 50.0)
        self.mock_inventory.get_stock.return_value = 10
        self.mock_payment.charge.side_effect = Exception("Connection refused")

        with self.assertRaises(PaymentFailedError):
            self.order.checkout()

if __name__ == '__main__':
    unittest.main()
