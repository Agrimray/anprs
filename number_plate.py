'''import cv2

harcascade = "model/haarcascade_russian_plate_number.xml"

cap = cv2.VideoCapture(0)

cap.set(3, 640) # width
cap.set(4, 480) #height

min_area = 500
count = 0

while True:
    success, img = cap.read()

    plate_cascade = cv2.CascadeClassifier(harcascade)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    plates = plate_cascade.detectMultiScale(img_gray, 1.1, 4)

    for (x,y,w,h) in plates:
        area = w * h

        if area > min_area:
            cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
            cv2.putText(img, "Number Plate", (x,y-5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 255), 2)

            img_roi = img[y: y+h, x:x+w]
            cv2.imshow("ROI", img_roi)


    
    cv2.imshow("Result", img)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("plates/scaned_img_" + str(count) + ".jpg", img_roi)
        cv2.rectangle(img, (0,200), (640,300), (0,255,0), cv2.FILLED)
        cv2.putText(img, "Plate Saved", (150, 265), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255), 2)
        cv2.imshow("Results",img)
        cv2.waitKey(500)
        count += 1

'''

#till now best
'''
import cv2
import easyocr

harcascade = "model/haarcascade_russian_plate_number.xml"

cap = cv2.VideoCapture(0)

cap.set(3, 640)  # width
cap.set(4, 480)  # height

min_area = 500
count = 0

reader = easyocr.Reader(['en'])  # Initialize EasyOCR with English language support

while True:
    success, img = cap.read()

    plate_cascade = cv2.CascadeClassifier(harcascade)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    plates = plate_cascade.detectMultiScale(img_gray, 1.1, 4)

    for (x, y, w, h) in plates:
        area = w * h

        if area > min_area:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(img, "Number Plate", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 255), 2)

            img_roi = img[y: y + h, x:x + w]

            # Recognize the number plate using EasyOCR
            results = reader.readtext(img_roi)

            if results:
                number_plate_text = results[0][1]  # Get the recognized text
                cv2.putText(img, "Plate Text: " + number_plate_text, (x, y - 30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1,
                            (255, 0, 0), 2)

    cv2.imshow("Result", img)

    key = cv2.waitKey(1)

    if key & 0xFF == ord('s'):
        if 'img_roi' in locals():
            cv2.imwrite("plates/scaned_img_" + str(count) + ".jpg", img_roi)
            cv2.rectangle(img, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, "Plate Saved", (150, 265), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255), 2)
            cv2.imshow("Results", img)
            cv2.waitKey(500)

            # Use EasyOCR to recognize the saved plate
            saved_plate_results = reader.readtext(img_roi)

            if saved_plate_results:
                saved_plate_text = saved_plate_results[0][1]
                print("Saved Plate Text:", saved_plate_text)

            count += 1

    elif key == 27:  # Press 'Esc' key to exit
        break

cap.release()
cv2.destroyAllWindows()'''
import cv2
import easyocr

harcascade = "model/haarcascade_russian_plate_number.xml"

cap = cv2.VideoCapture(0)

cap.set(3, 640)  # width
cap.set(4, 480)  # height

min_area = 500
count = 0

reader = easyocr.Reader(['en'])  # Initialize EasyOCR with English language support

while True:
    success, img = cap.read()

    plate_cascade = cv2.CascadeClassifier(harcascade)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    plates = plate_cascade.detectMultiScale(img_gray, 1.1, 4)

    for (x, y, w, h) in plates:
        area = w * h

        if area > min_area:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(img, "Number Plate", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 255), 2)

            img_roi = img[y: y + h, x:x + w]

            # Recognize the number plate using EasyOCR
            results = reader.readtext(img_roi)

            if results:
                number_plate_text = results[0][1]  # Get the recognized text
                cv2.putText(img, "Plate Text: " + number_plate_text, (x, y - 30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1,
                            (255, 0, 0), 2)

                # Save the image with the real number plate text
                img_filename = "plates/scaned_img_" + number_plate_text + ".jpg"
                cv2.imwrite(img_filename, img_roi)
                print("Saved Plate Text:", number_plate_text)

    cv2.imshow("Result", img)

    key = cv2.waitKey(1)

    if key == 27:  # Press 'Esc' key to exit
        break

cap.release()
cv2.destroyAllWindows()

