﻿/*
 * Created by SharpDevelop.
 * User: yyuso
 * Date: 17/3/2017
 * Time: 09:35
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
namespace UDPserver
{
	partial class MainForm
	{
		/// <summary>
		/// Designer variable used to keep track of non-visual components.
		/// </summary>
		private System.ComponentModel.IContainer components = null;
		private System.Windows.Forms.ListBox lbConnections;
		
		/// <summary>
		/// Disposes resources used by the form.
		/// </summary>
		/// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
		protected override void Dispose(bool disposing)
		{
			if (disposing) {
				if (components != null) {
					components.Dispose();
				}
			}
			base.Dispose(disposing);
		}
		
		/// <summary>
		/// This method is required for Windows Forms designer support.
		/// Do not change the method contents inside the source code editor. The Forms designer might
		/// not be able to load this method if it was changed manually.
		/// </summary>
		private void InitializeComponent()
		{
			System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(MainForm));
			this.lbConnections = new System.Windows.Forms.ListBox();
			this.SuspendLayout();
			// 
			// lbConnections
			// 
			this.lbConnections.FormattingEnabled = true;
			this.lbConnections.Location = new System.Drawing.Point(12, 12);
			this.lbConnections.Name = "lbConnections";
			this.lbConnections.Size = new System.Drawing.Size(260, 238);
			this.lbConnections.TabIndex = 0;
			// 
			// MainForm
			// 
			this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.ClientSize = new System.Drawing.Size(284, 261);
			this.Controls.Add(this.lbConnections);
			this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
			this.Name = "MainForm";
			this.Text = "UDPserver";
			this.Load += new System.EventHandler(this.MainFormLoad);
			this.ResumeLayout(false);

		}
	}
}
