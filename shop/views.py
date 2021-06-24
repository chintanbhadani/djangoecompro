from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Contact,Orders
from math import ceil
from json import dumps
from django.core import serializers
import razorpay
import json

from django.views.decorators.csrf import csrf_exempt
# from PayTm import Checksum
# Create your views here.
# from django.http import HttpResponse
MERCHANT_KEY = 'Your-Merchant-Key-Here'

# Create your views here.
def index(request):
    # return HttpResponse("Index Shop")
    # params = {'purpose':'Remove Punctuations','analyzed_text':analyze}
    # return render(request,'analyse.html',params)
    json_serializer = serializers.get_serializer("json")()
    jsonproducts = json_serializer.serialize(Product.objects.all())


    products = Product.objects.all()
    print(products)
    n = len(products)
    nSlides = n//4 + ceil((n/4)-(n//4))
    print(n)
    print(nSlides)
    # print(products[4].image)
    
    allProds = []
    catprods = Product.objects.values('catagory')
    print("catprods   ",catprods)
    cats = { item['catagory'] for item in catprods }
    for cat in cats:
        prod = Product.objects.filter(catagory=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    print(allProds)    

    # params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products,'allProds':allProds}
    params = {'allProds':allProds,'product':jsonproducts}

    return render(request, 'index3.html',params)
    # return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name1')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        print(name)
        print(email)
        print(desc)
        contact = Contact(name=name,email=email,desc=desc)
        contact.save()
    return render(request,'contact.html')    

def tracker(request):
    return render(request,'tracker.html')    

def search(request):
    return render(request,'search.html')   

def cart(request):
    json_serializer = serializers.get_serializer("json")()
    products = json_serializer.serialize(Product.objects.all())
    # products = Product.objects.all()
    # dataJSON = dumps(products)
    params3 = {'product':products}
    return render(request,'productview.html',params3)   

def productview(request,myid):
    product = Product.objects.filter(id=myid)
    params2 = {'product':product[0]}
    print(product[0])
    return render(request,'productview2.html',params2)


# def checkout(request):
#     return render(request,'checkout.html')
@csrf_exempt
def checkout(request):
    if request.method=="POST":
        
        print(request.POST.get('name', ''))
        print(request.POST.get('itemsJson', ''))
        print(request.POST.get('email', ''))
        print(request.POST.get('amount', ''))

        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        amount = request.POST.get('amount', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')

        # order = Orders(items_json=items_json, name=name, email=email, address=address, city=city,
        #                state=state, zip_code=zip_code, phone=phone, amount=amount)
        # order.save()

        
        client = razorpay.Client(auth=("rzp_test_nL2qSed9iwqMSv", "7RvorULiPiTpk5dIugPuFUiN"))

        order_amount = int(amount) 
        order_currency = 'INR'
        order_receipt = 'order_rcptid_11'
        notes = {'Shipping address': 'Bommanahalli, Bangalore'}   # OPTIONAL
        # receipt=order_receipt             ,payment_capture=1 

        payment = client.order.create({'amount':order_amount, 'currency':order_currency, 'notes':notes, 'payment_capture':'1'})
        print(payment)
        

        param = json.dumps(payment)

        # json_serializer = serializers.get_serializer("json")()
        # param = json_serializer.serialize(payment)

        paymentparams = {'payment' : param}

        return render(request, 'checkout.html', paymentparams)


        # update = OrderUpdate(order_id=order.order_id, update_desc="The order has been placed")
        # update.save()
        # thank = True
        # id = order.order_id
        # # return render(request, 'shop/checkout.html', {'thank':thank, 'id': id})
        # # Request paytm to transfer the amount to your account after payment by user
        # param_dict = {
        #         'MID': 'Your-Merchant-Id-Here',
        #         'ORDER_ID': str(order.order_id),
        #         'TXN_AMOUNT': str(amount),
        #         'CUST_ID': email,
        #         'INDUSTRY_TYPE_ID': 'Retail',
        #         'WEBSITE': 'WEBSTAGING',
        #         'CHANNEL_ID': 'WEB',
        #         'CALLBACK_URL':'http://127.0.0.1:8000/shop/handlerequest/',

        # }
        # param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
        # return render(request, 'shop/paytm.html', {'param_dict': param_dict})

    return render(request, 'checkout.html')


# def paymentSuccess:
    #   return HttpResponse("Index Shop")
    
@csrf_exempt
def sucess(request):
    return render(request, 'sucess.html')

          


@csrf_exempt
def handlerequest(request):
    # paytm will send you post request here
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]

    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order successful')
        else:
            print('order was not successful because' + response_dict['RESPMSG'])
    return render(request, 'shop/paymentstatus.html', {'response': response_dict})    

    