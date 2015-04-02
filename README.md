# KTree_Odoo-Magento-Connector
A full fledged KTree Odoo-Magento Connector featured with all the functionality and capable of syncing the data between two stand alone systems(Odoo-Magento) without any data loss

                        ktree_magento_connector version 1.0  24/03/2015

Odoo is an open source e-commerce/ERP application software that supports integration with numerous other software applications. 
Odoo is suite of open source Business Apps which include e-commerce,CRM,Purchase , Sales ,Warehouse ,Accounting ,Warehouse ,Project Management , Marketing , Employee Management & manufacturing.
Whenever an ERP is intended to associate with the Company's Web Site for E- Commerce perspective, Magento integrates with Odoo, where Magento is a powerful, out-of the-box, rich in features, e-commerce tool used for E-Commerce web-site development. Hence the integration of Odoo with Magento provides multi functional capability to the web site with robust Shopping cart experience whereas Magento enacts efficient Front end platform for the web shop while Odoo operates as perfect back office Application.Odoo integration with Magento supports all business functions required by an enterprise.

KTree avails best-of-breed solutions to integrate Odoo and Magento. Our expertised team is specialized on Odoo and has experience in integrating services with web applications and also has demonstrative understanding of the underlying technologies resulting in excellent business management and growth.

The module KTree developed has the following features:

Magento to Odoo sync:
Magento Order will be created as a new Sales quotation/order in Odoo automatically.
Customer/s created in Magento will get imported to Odoo.
Product/s ( Simple and Bundled) created in Magento will be imported to Oooo.
Any update to Product attributes in Magento will get updated to Odoo.

Odoo to Magento sync:
Odoo will host as a stock master and will continuously update Magento Stock.
Real stock of every product will be updated from Odoo to Magento. Quantity in hand in Odoo will be synced to Magento based on the Sales and purchases.
Any updates to Customer in Odoo will get synced back to Magento
Any updates to Product in Odoo will get synced back to Magento
Invoices synch back to Magento from Odoo
Delivery order synch back to magento from odoo

Technical Detail:

- The ktree_magento_connector module is build with the help of the source codes available in lunchpad, github.

  Compatible with Odoo 8 and the Magento versions 1.7 or later
  
- This module is having a dependancy on product_images_olbs which is available on odoo apps.

- A new custom KTree developed API on magento end which is more flexible for synchronization process between the two stand alone application i.e magento and odoo..

- Magento custome API Ktree_Customapi-0.1.0.tgz which needs to be installed at magento side before proceeding for Synchronization.

- Place the ktree_magento_connector module in odoo 8 addons and install it.

- create a API user at magento with all role based access rights.

- Configure the magento api details on odoo under the menu called  Magento--> Magento settings.


