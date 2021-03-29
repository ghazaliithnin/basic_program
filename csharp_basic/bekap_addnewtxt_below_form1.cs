using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace add_newtxtbox_below
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        int c = 0; // for unique txtDynamic text creation
        private void button1_Click(object sender, EventArgs e)
        {
            TextBox txtDynamic = this.Controls.Find("txtDynamic" + c, true)[0] as TextBox; // find lastly added txtDynamic 

            TextBox txtRun = new TextBox();
            c = c + 1;
            txtRun.Name = "txtDynamic" + ++c;
            //txtRun.Name = "txtDynamic" + c;
            txtRun.Size = new System.Drawing.Size(100, 20);
            txtRun.Location = new Point(txtDynamic.Location.X, txtDynamic.Location.Y + 35); // X axis will be same y will increase with count 35


            foreach (Control item in this.Controls)
            {
                if (item.Location.Y >= txtRun.Location.Y)
                { // if there is an item that has greater Y location
                    item.Location = new Point(item.Location.X, txtRun.Location.Y + 35); // It should increase its value as 35 too.
                }
                this.Controls.Add(txtRun);

            }
        }
    }
}
