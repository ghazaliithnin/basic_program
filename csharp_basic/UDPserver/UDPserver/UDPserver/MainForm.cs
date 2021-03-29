/*
 * Created by SharpDevelop.
 * User: yyuso
 * Date: 17/3/2017
 * Time: 09:35
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Net.Sockets;
using System.Net;
using System.Text;
using System.Windows.Forms;
using System.Threading;


namespace UDPserver
{
	/// <summary>
	/// Description of MainForm.
	/// </summary>
	public partial class MainForm : Form
	{
		
		public void serverThread()
		{
			UdpClient udpClient = new UdpClient(8080);
			while(true)
			{
				IPEndPoint RemoteIpEndPoint = new IPEndPoint(IPAddress.Any,0);
				Byte[] receiveBytes = udpClient.Receive(ref RemoteIpEndPoint);
				string returnData = Encoding.ASCII.GetString(receiveBytes);
				this.SetText(RemoteIpEndPoint.Address.ToString() + ":" + returnData.ToString()); 	
			}
		}

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
		
		void MainFormLoad(object sender, EventArgs e)
		{
			Thread thdUDPServer = new Thread(new ThreadStart(serverThread));
			thdUDPServer.Start();	 		
		}
		
		delegate void StringArgReturningVoidDelegate(string text);  
		
		
		private void SetText(string text)  
		{  
		    // InvokeRequired required compares the thread ID of the  
		    // calling thread to the thread ID of the creating thread.  
		    // If these threads are different, it returns true.  
		    if (this.lbConnections.InvokeRequired)  
		    {     
		        StringArgReturningVoidDelegate d = new StringArgReturningVoidDelegate(SetText);  
		        this.Invoke(d, new object[] { text });  
		    }  
		    else  
		    {  
		    	lbConnections.Items.Add(text);
		    }  
		}	
		
	} //
}
