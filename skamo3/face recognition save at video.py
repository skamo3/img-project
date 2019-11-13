
import cv2

#분석할 동영상 파일 
video_file_path = 'standing comedy.mp4'

# 동영상 파일 open
cap = cv2.VideoCapture(video_file_path)

#잘 열려있는지 확인
if cap.isOpened() == False :
    print("Can't open the video {}" .format(video_file_path))
    exit()

titles = ['orig']
#윈도우 생성 및 사이즈 변경
for t in titles :
    cv2.namedWindow(t)
#파일의 넓이
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
#파일의 높이
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
#파일의 프레임레이트
fps = cap.get(cv2.CAP_PROP_FPS)

print("width {}, height {}, fps {}".format(width,height,fps))

#저장할 비디오 코덱
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
#저장할 파일 이름
filename = 'standing comedy face recognition.mp4'

#파일 stream 생성
out = cv2.VideoWriter(filename, fourcc, fps, (int(width), int(height)))
#filename = 파일이름
#fourcc = 코덱
#fps = 초당 프레임 수
#width =넓이
#height = 높이

#얼굴 인식용
face_cascade = cv2.CascadeClassifier()
# CascadeClassifier.load를 할 때 들어갈 파일은 cv2를 다운받은 폴더 안에 있음 / 이름에 따라 기능이 달라짐 
face_cascade.load('C://Users//USER.DESKTOP-QQ2NR7I//Anaconda3//envs//py1//Lib//site-packages//cv2//data//haarcascade_frontalcatface.xml')

while True :
    #파일로부터 이미지 얻기
    ret, frame = cap.read()
    
    #재생이 끝나면 종료(더 이상 읽어올 이미지가 없음)
    if frame is None :
        break;
        
    #얼굴인식 영상처리
    grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grayframe,(5,5), 0)
    faces = face_cascade.detectMultiScale(blur, 1.8, 2, 0, (50,50))
    
    #원본 이미지에 얼굴 인식된 부분 표시
    for (x,y,w,h) in faces :
        cx = int(x+(w/2))
        cy = int(y+(h/2))
        cr = int(w/2)
        cv2.circle(frame,(cx,cy),cr,(0,255,0),3)
        
    #얼굴 인식된 이미지 화면 표시
    cv2.imshow(titles[0],frame)
    
    #인식된 이미지 파일로 저장
    out.write(frame)
    
    #1ms동안 키 입력 대기 q입력시 out
    if cv2.waitKey(1) == ord('q') :
        break;
        
#재생 파일 종료
cap.release()
#저장 파일 종료
out.release()
#윈도우 종료
cv2.destroyAllWindows()
    
        
        
        
        