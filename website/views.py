from django.shortcuts import render
from website.models import IMG

# Create your views here.

def uploadImg(request):
    if request.method == 'POST':
        IMG.objects.all().delete()
        import os
        import shutil
        path = os.getcwd()

        path += '/media/upload'
        print(path)
        try:
            if os.path.exists(path):
                pass
            else:
                os.makedirs(path)

            shutil.rmtree(path)
        finally:
            pass
        print(os.getcwd())
        new_img = IMG(
            img=request.FILES.get('img')
        )
        new_img.save()
    return render(request, 'uploadimg.html')

def runtest():
    import os
    os.system("python /home/xujiamin/chenfeilong/self-critical.pytorch/eval.py --model /home/xujiamin/chenfeilong/self-critical.pytorch/log_fc_rl/model.pth --infos_path /home/xujiamin/chenfeilong/self-critical.pytorch/log_fc_rl/infos_fc_rl.pkl --image_folder /home/xujiamin/chenfeilong/ImageCaption/media/upload --num_images -1")

def showImg(request):
    imgs = IMG.objects.all()
    content = {
        'imgs':imgs,
    }
    import os
    import threading
    t = threading.Thread(target=runtest)
    t.start()
    return render(request, 'showimg.html', content)

def show(content):
    return render('caption.html', content)

def index(request):
    return render(request, 'index.html')

def caption(request):
    return render(request, 'caption.html')
