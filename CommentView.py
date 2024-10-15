import tkinter as tk
from tkinter import ttk, messagebox
import StatusPredict

def on_comment_click(comment):
    if StatusPredict.pridiction_report(comment)[0] == 1:
        messagebox.showinfo("Thông báo", "Bình luận bình thường")
    elif StatusPredict.pridiction_report(comment)[0] == 0:
        messagebox.showinfo("Thông báo", "Bình luận tiêu cực")
    else:
        messagebox.showinfo("Thông báo", "Bình luận tích cực")

def create_window():
    root = tk.Tk()
    root.title("Comment Display")
    root.geometry("521x719")

    content_pane = ttk.Frame(root, padding=10)
    content_pane.grid()

    ttk.Label(content_pane, text="Comment", font=("Tahoma", 20, "bold")).grid(row=0, column=0, sticky="W", pady=10)

    comments = [
        ("Nguyễn Thị Quỳnh Hương", "Xấy Tóc", "Sản Phẩm này phù hợp với tôi, giá cả tốt. Tôi rất thích."),
        ("Trần Văn Thanh", "Áo Thun", "Giao hàng chậm, sản phẩm không như hình. Không lên mua."),
        ("Nguyễn Quang", "Kệ Sách", "Bình Thường. không có gì nổi bật.")
    ]

    for idx, (name, product, comment) in enumerate(comments, start=1):
        panel = ttk.Frame(content_pane, padding=10)
        panel.grid(row=idx, column=0, sticky="EW", pady=5)

        ttk.Label(panel, text=f"Name: {name}", font=("Tahoma", 13)).grid(row=0, column=0, sticky="W")
        ttk.Label(panel, text=f"Sản Phẩm: {product}", font=("Tahoma", 13)).grid(row=1, column=0, sticky="W")
        comment_label = ttk.Label(panel, text=f"Comment: {comment}", font=("Tahoma", 13), cursor="hand2")
        comment_label.grid(row=2, column=0, sticky="W")

        comment_label.bind("<Button-1>", lambda e, c=comment: on_comment_click(c))

    root.mainloop()

create_window()
