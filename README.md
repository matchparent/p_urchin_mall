# Urchin Mall

This is a resume back-end Django project.

Database Mysql, deployed on Railway. Django deployed on Oracle Cloud.

Apps include:

* addr:
  * Add new receiving address
  * Set address as default
  * Delete address
  * Get user's address list
* cart:
  * Add/remove item count in cart, remove item in cart
  * Get user's cart list
  * Delete all in user's cart
  * Get cart item count
* comment:
  * Pagination query comment list
* commodity:
  * Pagination query goods list
  * Goods detail
  * Flash sale goods list
  * Goods search
* menu:
  * Main menu list - Home page
  * Sub menu list - Home page
* order:
  * Create order from cart
  * Get order by order status(-1: all; 0: to be confirmed; 1: to be paid; 2:to be received; 3: finished)
  * Delete order
  * Get order detail
  * Update order status
* pay:
  * Call Alipay, start paying
  * Verify pay result, update order status and redirect to this application
* user:
  * Login
  * Get user profile
  * Update password
  * JWT enabled
