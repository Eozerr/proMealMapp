from django.shortcuts import render,redirect
from .models import User
from django.contrib import messages

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.filter(email=email).first()  # Veritabanında e-posta ile kullanıcı sorgulama

        if user is not None and user.password == password:  # Kullanıcı varsa ve şifre doğruysa
            # Giriş başarılı mesajını göster
            messages.success(request, 'Login successful!')
            return render(request, 'calculate.html', {'message': 'Login successful!'})
        else:
            # Kullanıcı adı veya şifre hatalı
            messages.error(request, 'Incorrect email or password. Please register or check your credentials.')
            return render(request, 'login.html', {'message': 'Incorrect email or password. Please register or check your credentials.'})
    else:
        return render(request, 'login.html')


    

def register(request):
    if request.method == 'POST':
        # Formdan gelen verileri al
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        birth_date = request.POST['birth_date']
        
        # Yeni kullanıcı nesnesi oluştur
        user = User(name=name, email=email, password=password, birth_date=birth_date)
        
        # Kullanıcıyı veritabanına kaydet
        user.save()
        
        return redirect('index')  # Kayıt başarılıysa ana sayfaya yönlendir
    
    return render(request, 'register.html')


def index(request):
    return render(request, 'index.html')

def calculate(request):
    return render(request, 'calculate.html')
