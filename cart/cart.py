from store.models import Product


class Cart():
    def __init__(self,request):
        self.session=request.session

        cart=self.session.get('session_key')

        if  'session_key' not in request.session:
            cart=self.session['session_key']={}

        self.cart=cart


    def add(self,product,quantity):
        product_id= str(product.id)
        product_qty=quantity

        if product_id in self.cart:
            pass
        else:
            self.cart[product_id]=int(product_qty)

        self.session.modified=True

    def __len__(self):
        return len(self.cart)
    
    def get_prod(self):
        product_ids=self.cart.keys()
        products=Product.objects.filter(id__in=product_ids)
        return products

    def get_quant(self):
        quantity=self.cart
        print(quantity)
        return quantity
    
    def update(self,product,Quantity):
        product_id=str(product)
        product_qty=int(Quantity)

        ourcart=self.cart
        ourcart[product_id]=product_qty

        self.session.modified=True
        thing=self.cart

        return thing
    
    def delete_item(self,Product_id):
        ourcart= self.cart
        print(f"The cart ***********{ourcart}")
    
        for key,value in ourcart.items():
            if key==Product_id:
                del ourcart[key]
                break

        self.session.modified=True
        thing =self.cart

        return thing
    
    def get_total(self):
        
        #getting the product ids
        product_ids=self.cart.keys()

        products=Product.objects.filter(id__in=product_ids)
        total=0
        ourcart=self.cart


        for key,value in ourcart.items():
            key=int(key)
            for product in products:
                if product.id==key:
                    if product.is_sale:
                        total=total+product.sale_price*value
                    else:
                        total=total+product.price*value



        #print("total",total)
        return total





