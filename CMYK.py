
class CMYK:

    def __init__(self):
        self.C = 0
        self.M = 0
        self.Y = 0
        self.K = 0


    def slider_C_ValueChanged(self):
    # update green
    # update blue
    background_m = np.zeros((22, 267, 4), dtype="uint8")
    background_g = np.zeros((22, 267, 4), dtype="uint8")
    width = 267
    height = 22

    for i in range(width):
        new_green = int((i / width) * 255)
        new_blue = int((i / width) * 255)

    # for j in range(height):
    #  background_b[j, i] = [new_blue, self.G_Slider.value(), self.R_Slider.value(), 100]
    # background_g[j, i] = [self.B_Slider.value(), new_green, self.R_Slider.value(), 100]

    cv2.imwrite('m_slider_background.jpg', background_m)
    cv2.imwrite('g_slider_background.jpg', background_g)
    self.M_Slider.setStyleSheet("QSlider {background-image: url(m_slider_background.jpg);}")
    self.B_Slider.setStyleSheet("QSlider {background-image: url(b_slider_background.jpg);}")


    def slider_M_ValueChanged(self):
    # update green
    # update blue
    background_m = np.zeros((22, 267, 4), dtype="uint8")
    background_g = np.zeros((22, 267, 4), dtype="uint8")
    width = 267
    height = 22

    for i in range(width):
        new_green = int((i / width) * 255)
        new_blue = int((i / width) * 255)

    # for j in range(height):
    #  background_b[j, i] = [new_blue, self.G_Slider.value(), self.R_Slider.value(), 100]
    # background_g[j, i] = [self.B_Slider.value(), new_green, self.R_Slider.value(), 100]

    cv2.imwrite('m_slider_background.jpg', background_m)
    cv2.imwrite('g_slider_background.jpg', background_g)
    self.M_Slider.setStyleSheet("QSlider {background-image: url(m_slider_background.jpg);}")
    self.B_Slider.setStyleSheet("QSlider {background-image: url(b_slider_background.jpg);}")


    def slider_Y_ValueChanged(self):
    # update green
    # update blue
    background_m = np.zeros((22, 267, 4), dtype="uint8")
    background_g = np.zeros((22, 267, 4), dtype="uint8")
    width = 267
    height = 22

    for i in range(width):
        new_green = int((i / width) * 255)
        new_blue = int((i / width) * 255)

    # for j in range(height):
    #  background_b[j, i] = [new_blue, self.G_Slider.value(), self.R_Slider.value(), 100]
    # background_g[j, i] = [self.B_Slider.value(), new_green, self.R_Slider.value(), 100]

    cv2.imwrite('m_slider_background.jpg', background_m)
    cv2.imwrite('g_slider_background.jpg', background_g)
    self.M_Slider.setStyleSheet("QSlider {background-image: url(m_slider_background.jpg);}")
    self.B_Slider.setStyleSheet("QSlider {background-image: url(b_slider_background.jpg);}")


    def slider_K_ValueChanged(self):
    # update green
    # update blue
    background_m = np.zeros((22, 267, 4), dtype="uint8")
    background_g = np.zeros((22, 267, 4), dtype="uint8")
    width = 267
    height = 22

    for i in range(width):
        new_green = int((i / width) * 255)
        new_blue = int((i / width) * 255)

    # for j in range(height):
    #  background_b[j, i] = [new_blue, self.G_Slider.value(), self.R_Slider.value(), 100]
    # background_g[j, i] = [self.B_Slider.value(), new_green, self.R_Slider.value(), 100]

    cv2.imwrite('m_slider_background.jpg', background_m)
    cv2.imwrite('g_slider_background.jpg', background_g)
    self.M_Slider.setStyleSheet("QSlider {background-image: url(m_slider_background.jpg);}")
    self.B_Slider.setStyleSheet("QSlider {background-image: url(b_slider_background.jpg);}")


