from tkinter import *
from fpdf import FPDF
window=Tk()
window.title(" Invoice Generator")

medicines={
    "Medicine A":10,
    "Medicine B":20,
    "Medicine C":15,
    "Medicine D":25,
}
invoice_item=[]
def add_medicine():
    selected_medicine=medicine_listbox.get(ANCHOR)  #it gives that u have selected from mouse on the tkinter window 
    quantity=int(quantity_entry.get())
    price=medicines[selected_medicine]   # selected_medicine has medicine A in it and once we write medicines[selected_medicine] we get the value of it
    item_total=price*quantity
    invoice_item.append((selected_medicine,quantity,item_total))
    total_amount_entry.delete(0,END)
    total_amount_entry.insert(END,str(calculate_total()))
    update_invoice_text()

def calculate_total():
    total=0.0
    for item in invoice_item:
        total=total+item[2]
    return total    


def update_invoice_text():
    invoice_text.delete(1.0,END)  #1.0 represents 1 is the line number and 0 is the column number
    for item in invoice_item:
        invoice_text.insert(END,f"Medicine:{item[0]},Quantity:{item[1]},Total:{item[2]}\n")     # END means very beginning, we have to show 3 things in invoice text and its in the order of medicine quantity and total so [0] represents medicine 1 represents qauntity and 2 represents price

 
def Generate_invoice():
    customer_name=customer_entry.get()
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("helvetica",size=12)
    pdf.cell(0,10,text="Invoice",new_x="LMARGIN",new_y="NEXT",align="C")  # NEXT means new line
    pdf.cell(0,10,text="Customer:"+customer_name,new_x="LMARGIN",new_y="NEXT",align="L")
    pdf.cell(0,10,text="",new_x="LMARGIN",new_y="NEXT")
    for item in invoice_item:
        medicine_name,quantity,item_total=item
        pdf.cell(0,10,text=f"Medicine:{medicine_name},Quantity:{quantity},total:{item_total}",new_x="LMARGIN",new_y="NEXT",align="L")

    pdf.cell(0,10,text="Total Amount:"+str(calculate_total()),new_x="LMARGIN",new_y="NEXT",align="L")

    pdf.output("invoice.pdf")        
    


medicine_label=Label(window,text="Medicine")
medicine_label.pack()

medicine_listbox=Listbox(window,selectmode=SINGLE)    # listbox is used to display a list of items,selectmode is used so as to select a single item
for medicine in medicines:
    medicine_listbox.insert(END,medicine)# END means u have to insert the element at starting point

medicine_listbox.pack()

quantity_label=Label(window,text="Quantity")
quantity_label.pack()

quantity_entry=Entry(window)
quantity_entry.pack()

add_button=Button(window,text="Add Medecine",command=add_medicine)
add_button.pack()

total_amount_label=Label(window,text="Total Amount")
total_amount_label.pack()
total_amount_entry=Entry(window)
total_amount_entry.pack()

customer_label=Label(window,text="Customer Name:")
customer_label.pack()
customer_entry=Entry(window)
customer_entry.pack()

generate_button=Button(window,text="Generate Invoice",command=Generate_invoice)
generate_button.pack()


invoice_text=Text(window,height=10,width=50)
invoice_text.pack()


window.mainloop()