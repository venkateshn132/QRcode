#!/usr/bin/env python
# coding: utf-8

# In[1]:


import qrcode


# In[2]:


qr = qrcode.QRCode(
    version=40,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=2,
    border=4,
)
s=input("Enter the text:")
qr.add_data(s)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="aqua")
img.save("m.png")


# In[3]:


img


# In[ ]:




