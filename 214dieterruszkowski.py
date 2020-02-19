import tkinter as tk
# main window

root = tk.Tk()
root.wm_geometry("200x200")
root.title("authorization")

frame_auth = tk.Frame(root)
frame_auth.grid(row= 0,column= 0, sticky="news")

frame_login = tk.Frame(root)
frame_login.grid()

lbl_username = tk.Label(frame_login, text='Username:')
lbl_username.pack(padx=50)


lbl_password = tk.Label(frame_login, text='Password:')
lbl_password.pack(padx=50)

ent_password = tk.Entry(frame_login, bd=3, show='*')
ent_password.pack()

ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack()


button_login = tk.Button(frame_login, text="Login")
button_login.pack()


frame_auth = tk.Frame(root)
frame_auth.grid(row= 0,column= 0, sticky="news")


root.mainloop()