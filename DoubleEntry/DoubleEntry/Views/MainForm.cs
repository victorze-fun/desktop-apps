using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace DoubleEntry.Views
{
    public partial class MainForm : Form
    {
        public MainForm()
        {
            InitializeComponent();
        }

        private void formToolStripMenuItem_Click(object sender, EventArgs e)
        {
            var dayBookForm = new DayBookForm();
            dayBookForm.ShowDialog();
        }
    }
}
