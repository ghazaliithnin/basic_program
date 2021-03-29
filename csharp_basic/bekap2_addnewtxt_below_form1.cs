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
        int pic_c = 0;

        int y_txtRun = 120;

        private void button1_Click(object sender, EventArgs e)
        {
            // find lastly added txtDynamic
            TextBox txtDynamic = this.Controls.Find("txtDynamic" + c, true)[0] as TextBox; 
            TextBox txtRun = new TextBox();

            // find lastly added picBox

            PictureBox picBox = this.Controls.Find("picBox" + pic_c, true)[0] as PictureBox;
            PictureBox picBoxRun = new PictureBox();


            c = c + 1; // Increment counter txtDynamic
            pic_c = pic_c + 1; // Increment for picture Box dynamic

            // Add Text Box Dynamically
            txtRun.Name = "txtDynamic" + c;
            txtRun.Size = new System.Drawing.Size(138,22);

            // Location for new text box
            // X axis will be same, Y will increase with count 35
            txtRun.Location = new Point(txtDynamic.Location.X, txtDynamic.Location.Y + y_txtRun); //35

            // Add Pic Box Dynamically
            picBoxRun.Name = "picBox" + pic_c;
            picBoxRun.Size = new System.Drawing.Size(100, 100);
            picBoxRun.BorderStyle = BorderStyle.FixedSingle;
            picBoxRun.Location = new Point(picBox.Location.X, picBox.Location.Y + 120); // 35 // Location for new pic box

            foreach (Control item in this.Controls)
            {
                if (item.Location.Y >= txtRun.Location.Y)
                {
                    //if there is an item that has greater Y location
                    item.Location = new Point(item.Location.X, txtRun.Location.Y + y_txtRun);//35  // it should increase its value as 35 too.

                }
                this.Controls.Add(txtRun);

                if (item.Location.Y >= picBoxRun.Location.Y)
                {
                    item.Location = new Point(item.Location.X, picBoxRun.Location.Y + 120); // 35
                }
                this.Controls.Add(picBoxRun);
            }

        }
    }
}
