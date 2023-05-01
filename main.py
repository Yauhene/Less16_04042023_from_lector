import cv2

#img = cv2.imread('D:\Jack\Java II/test.jpg')
img = cv2.imread('test.jpg')
print(img)

#cv2.imshow('test.jpg', img)
#cv2.waitKey(3000)


img = cv2.resize(img, (300, 500))
print(img.shape)
cv2.imshow('Result', img)
cv2.waitKey(3000)

print(img.shape)
# сохраняем размер картинки в списке 
dim_list = list(img.shape)
for i in range(len(dim_list)):
    print(f'dim_list[{i}] = {dim_list[i]}, {type(dim_list[i])}')
print(f'список с размерами картинки test.jpg: {dim_list}')

krat = 0.5 # вводим коэффициент (масштаб)

img = cv2.resize(img, (int(dim_list[1] * krat), int(dim_list[0] * krat)))
print(img.shape)
cv2.imshow('Во какая фигня вышла!', img)
cv2.waitKey(3000)

print(img.shape)

