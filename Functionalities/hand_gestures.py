import webbrowser
import cv2
def Camera():
    cam = cv2.VideoCapture(0)
    from mediapipe import solutions as sol
    mph = sol.hands
    mpdraw = sol.drawing_utils
    mpstyle = sol.drawing_styles
    hand_conn = mpstyle.get_default_hand_connections_style
    hand_lm = mpstyle.get_default_hand_landmarks_style
    hand_detect = mph.Hands(min_detection_confidence=0.5)

    old_value=0
    while True:
        r, im = cam.read()
        if r == True:
            im = cv2.flip(im, 1)
            ##print(im.shape)
            results = hand_detect.process(im)
            counter = 0
            if results.multi_hand_landmarks:
                for gesture in results.multi_hand_landmarks:
                    mpdraw.draw_landmarks(
                        im, gesture, mph.HAND_CONNECTIONS, hand_lm(), hand_conn() 
                    )

                    if gesture.landmark[8].y < gesture.landmark[5].y:
                            counter += 1
                    if gesture.landmark[12].y < gesture.landmark[9].y:
                            counter += 1
                    if gesture.landmark[16].y < gesture.landmark[13].y:
                            counter += 1
                    if gesture.landmark[20].y < gesture.landmark[17].y:
                            counter += 1
                        
            print(counter)
            if counter == 1 and old_value != counter:
                webbrowser.open('www.amazon.com')
            old_value = counter

            if counter == 2 and old_value != counter:
                webbrowser.open('www.facebook.com')
            old_value = counter
            
            if counter == 3 and old_value != counter:
                webbrowser.open('www.instagram.com')
            old_value = counter
            
            if counter == 4 and old_value != counter:
                webbrowser.open('www.linkedin.com')
            old_value = counter                       
            cv2.imshow('samplestream', im)
            
            if cv2.waitKey(1) == ord('a'):
                break
    cam.release()
    cv2.destroyAllWindows()