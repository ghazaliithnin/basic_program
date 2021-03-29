/*
 * Created by SharpDevelop.
 * User: yyuso
 * Date: 17/3/2017
 * Time: 09:28
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
using System;
using System.Collections.Generic;
using System.Drawing;
using  System.Net.Sockets;
using System.Text;
using System.Windows.Forms;

namespace UDPclient
{
	/// <summary>
	/// Description of MainForm.
	/// </summary>
	public partial class MainForm : Form
	{
		public MainForm()
		{
			//
			// The InitializeComponent() call is required for Windows Forms designer support.
			//
			InitializeComponent();
			
			//
			// TODO: Add constructor code after the InitializeComponent() call.
			//
		}
		void BtnSendClick(object sender, EventArgs e)
		{
			UdpClient udpClient = new UdpClient();
			udpClient.Connect(txtbHost.Text, 8080); // 8080
			Byte[] senddata = Encoding.ASCII.GetBytes("Hello World");
			udpClient.Send(senddata, senddata.Length);
		}
	}
}
