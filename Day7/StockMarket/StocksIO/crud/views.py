from django.shortcuts import render, get_object_or_404, redirect
from .models import Stock, UserStock
from django.contrib.auth.models import User
from django import forms
from .utils import get_tiingo_price, get_tiingo_profile, search_tiingo
from django.contrib import messages

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['ticker', 'name', 'curr_price', 'description']

def stock_list(request):
    query = request.GET.get('q', '')
    stocks = Stock.objects.all()
    if query:
        stocks = stocks.filter(ticker__icontains=query) | stocks.filter(name__icontains=query)
    stock_data = []
    for stock in stocks:
        live_price = get_tiingo_price(stock.ticker)
        profile = get_tiingo_profile(stock.ticker)
        stock_data.append({
            'stock': stock,
            'live_price': live_price,
            'profile': profile
        })
    return render(request, 'crud/stock_list.html', {
        'stock_data': stock_data,
        'query': query
    })

def stock_search(request):
    query = request.GET.get('q', '')
    results = []
    if query:
        results = search_tiingo(query)
    return render(request, 'crud/stock_search.html', {'results': results, 'query': query})

def buy_stock(request, ticker):
    stock = get_object_or_404(Stock, ticker=ticker)
    if request.method == 'POST':
        price = get_tiingo_price(ticker)
        quantity = int(request.POST.get('quantity', 1))
        UserStock.objects.create(
            stock=stock,
            user=request.user,
            buy_price=price,
            purchase_date='2025-06-25',
            purchase_quantity=quantity
        )
        messages.success(request, f"Bought {quantity} shares of {ticker} at ₹{price}")
        return redirect('stock_list')
    return render(request, 'crud/buy_stock.html', {'stock': stock})

def watch_stock(request, ticker):
    # Implement your own logic to "watch" a stock (e.g., save to a Watchlist model)
    messages.success(request, f"Added {ticker} to your watchlist!")
    return redirect('stock_list')

def stock_create(request):
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            stock = form.save(commit=False)
            # Optionally fetch live data from Tiingo
            profile = get_tiingo_profile(stock.ticker)
            price = get_tiingo_price(stock.ticker)
            if profile:
                stock.name = profile.get('name', stock.name)
                stock.description = profile.get('description', stock.description)
            if price:
                stock.curr_price = price
            stock.save()
            return redirect('stock_list')
    else:
        form = StockForm()
    return render(request, 'crud/stock_form.html', {'form': form})

def stock_update(request, pk):
    stock = get_object_or_404(Stock, pk=pk)
    if request.method == 'POST':
        form = StockForm(request.POST, instance=stock)
        if form.is_valid():
            stock = form.save(commit=False)
            # Optionally update with live Tiingo data
            profile = get_tiingo_profile(stock.ticker)
            price = get_tiingo_price(stock.ticker)
            if profile:
                stock.name = profile.get('name', stock.name)
                stock.description = profile.get('description', stock.description)
            if price:
                stock.curr_price = price
            stock.save()
            return redirect('stock_list')
    else:
        form = StockForm(instance=stock)
    return render(request, 'crud/stock_form.html', {'form': form})

def stock_delete(request, pk):
    stock = get_object_or_404(Stock, pk=pk)
    if request.method == 'POST':
        stock.delete()
        return redirect('stock_list')
    return render(request, 'crud/stock_confirm_delete.html', {'stock': stock})
