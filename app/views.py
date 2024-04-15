from django.shortcuts import render,redirect
from .models import User
from django.contrib import messages
from django.contrib.auth import logout as django_logout
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login,logout

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.filter(email=email).first()  # Veritabanında e-posta ile kullanıcı sorgulama

        if user is not None and user.password == password:  # Kullanıcı varsa ve şifre doğruysa
            request.session['is_authenticated'] = True
            # Giriş başarılı mesajını göster
            messages.success(request, 'Login successful!')
            return render(request, 'calculate.html', {'message': 'Login successful!', 'user': request.user})
        else:
            # Kullanıcı adı veya şifre hatalı
            messages.error(request, 'Incorrect email or password. Please register or check your credentials.')
            return render(request, 'login.html', {'message': 'Incorrect email or password. Please register or check your credentials.'})
    else:
        return render(request, 'login.html')

def custom_logout(request):
    if request.session.get('is_authenticated'):
        request.session['is_authenticated'] = False
        logout(request)
        messages.success(request, 'Logged out successfully!')
    else:
        # Oturum zaten kapalıysa başka bir işlem yapmayabiliriz
        messages.error(request, 'You are not logged in!')
    return redirect('index')
    

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

def logout(request):
    django_logout(request)
    return redirect('index')
