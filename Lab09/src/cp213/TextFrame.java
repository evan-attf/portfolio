package cp213;

// Evan Attfield
// 180817010

/**
 * Class TextFrame - A frame that allows a user to open a text file into its
 * text area and edit or copy the text. The user may save the contents of the
 * file.
 *
 * @author <a href="http://javaalmanac.com">The Java Developers Almanac 1.4 </a>
 * @author <a href="http://www.akadia.com/services/java_xml_parser.html">XML
 *         Processing using XERCES Java Parser </a>
 * @author modified by David Brown
 * @version 2012-11-02
 */

// Imports

import java.awt.Font;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;
import javax.swing.JFileChooser;
import javax.swing.JFrame;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
import javax.swing.JOptionPane;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;

// --------------------------------------------------------------------

@SuppressWarnings("serial")
public class TextFrame extends JFrame {

	// --------------------------------------------------------------------
	/**
	 * @param args
	 *            Unused.
	 */
	public static void main(String[] args) {
		TextFrame output = new TextFrame("Simple Text Editor");
		output.setVisible(true);
	}

	// --------------------------------------------------------------------
	// Define the list of acceptable file extensions.

	public static final String[] EXTENSIONS = { "txt" };
	public static final String DESCRIPTION = "Text Files (*.txt)";

	private final JFileChooser chooser = new JFileChooser();
	private final JMenu editMenu = new JMenu("Edit");
	private final JMenuItem editMenuCopy = new JMenuItem("Copy");
	private final JMenuItem editMenuCopyAll = new JMenuItem("Copy All");
	private final JMenuItem editMenuWrap = new JMenuItem("Wrap");
	private final JMenu fileMenu = new JMenu("File");
	private final JMenuItem fileMenuExit = new JMenuItem("Exit");
	private final JMenuItem fileMenuOpen = new JMenuItem("Open");
	private final JMenuItem fileMenuSave = new JMenuItem("Save As");

	private final JMenuItem editMenuIndent = new JMenuItem("Indent");
	private final JMenu infoMenu = new JMenu("Info");
	private final JMenuItem infoMenuLineCount = new JMenuItem("Line Count");
	private final JMenuItem infoMenuWordCount = new JMenuItem("Word Count");
	private final JMenuBar menuBar = new JMenuBar();

	/**
	 * Defines the frame's text area.
	 */
	private final JTextArea textArea = new JTextArea(80, 20);

	/**
	 * Places the text area inside a scroll bar pane.
	 */
	private final JScrollPane textScroll = new JScrollPane(this.textArea);

	// --------------------------------------------------------------------
	/**
	 * The TextFrame constructor.
	 *
	 * @param title
	 *            The title to display on the frame.
	 */
	public TextFrame(String title) {
		this.setTitle(title);
		// Define the file chooser filter.

		// The file chooser may not display "All Files" as an option.
		this.chooser.setAcceptAllFileFilterUsed(false);
		this.layoutView();
		this.registerListeners();
	}

	// --------------------------------------------------------------------
	/**
	 * Lays out the contents of the frame.
	 */
	private void layoutView() {
		// Set a monospaced font for the text area.
		this.textArea.setFont(new Font("Monospaced", Font.PLAIN, 14));
		// Wrap text on word boundaries within the text area.
		this.textArea.setWrapStyleWord(true);
		// Forbid the text area to wrap its contents.
		this.textArea.setLineWrap(false);

		// Add the scroll bar pane (and its included text area) to the frame.
		this.getContentPane().add(this.textScroll);

		// Add the file options to the File menu.
		this.fileMenu.add(this.fileMenuOpen);
		this.fileMenu.add(this.fileMenuSave);
		this.fileMenu.add(this.fileMenuExit);
		// Add the File heading to the menu bar.
		this.menuBar.add(this.fileMenu);

		// Add the editing options to the Edit menu.
		this.editMenu.add(this.editMenuCopy);
		this.editMenu.add(this.editMenuCopyAll);
		this.editMenu.add(this.editMenuWrap);
		this.editMenu.add(this.editMenuIndent);
		// Add the Edit heading to the menu bar.
		this.menuBar.add(this.editMenu);

		this.menuBar.add(this.infoMenu);
		this.infoMenu.add(this.infoMenuLineCount);
		this.infoMenu.add(this.infoMenuWordCount);
		// Attach the menu bar to the frame.
		this.setJMenuBar(this.menuBar);

		// Set the size of the frame.
		this.setSize(800, 400);
	}

	// --------------------------------------------------------------------
	/**
	 * Pops up a dialog box to save the contents of the text area. Modified from
	 * <i>Developing Java Software, 2nd Edition </i> by Winder and Roberts.
	 */
	private void openFile() {
		File file = null;

		if (this.chooser.showOpenDialog(this) == JFileChooser.APPROVE_OPTION) {
			try {
				// Grab the file select and open it with a buffer.
				file = this.chooser.getSelectedFile();
				Scanner stream = new Scanner(file);

				while (stream.hasNextLine()) {
					this.textArea.append(stream.nextLine());
					// Required for line break in a JTextArea.
					this.textArea.append("\n");
				}
				stream.close();
			} catch (IOException e) {
				JOptionPane.showMessageDialog(null, "Could not read from file " + file.getName(), "Error",
						JOptionPane.ERROR_MESSAGE);
			}
		}
	}

	// --------------------------------------------------------------------
	/**
	 * Attaches listeners to the frames menu items.
	 */
	private void registerListeners() {

		this.editMenuCopy.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				TextFrame.this.textArea.copy();
				TextFrame.this.textArea.requestFocus();
			}
		});

		this.editMenuCopyAll.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				TextFrame.this.textArea.selectAll();
				TextFrame.this.textArea.copy();
				TextFrame.this.textArea.requestFocus();
			}
		});

		this.editMenuWrap.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				// Toggle the current line wrap setting.
				TextFrame.this.textArea.setLineWrap(!TextFrame.this.textArea.getLineWrap());
			}
		});

		this.fileMenuOpen.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				TextFrame.this.openFile();
			}
		});

		this.fileMenuSave.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				TextFrame.this.saveFile();
			}
		});

		this.fileMenuExit.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				TextFrame.this.dispose();
				System.exit(0);
			}
		});

		this.editMenuIndent.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				Scanner lineScanner = new Scanner(textArea.getText());
				String iText = "";
				
				while (lineScanner.hasNextLine()) {
					iText += "\t" + lineScanner.nextLine() + "\n";
				}
				
				TextFrame.this.textArea.setText(iText);
				TextFrame.this.textArea.setLineWrap(true);
				
				lineScanner.close();
			}

		});

		this.infoMenuLineCount.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				int lines = TextFrame.this.textArea.getLineCount();

				JOptionPane.showMessageDialog(null, "Line Count: " + lines);
			}
		});

		this.infoMenuWordCount.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				Scanner lineScanner = new Scanner(textArea.getText());
				int count = 0;

				while (lineScanner.hasNext()) {
					count++;
					lineScanner.next();
				}
				
				JOptionPane.showMessageDialog(null, "Word Count: " + count);
				lineScanner.close();
			}

		});
	}

	// --------------------------------------------------------------------
	/**
	 * Pops up a dialog box to save the contents of the text area. Taken from
	 * <i>Developing Java Software, 2nd Edition </i> by Winder and Roberts.
	 */
	private void saveFile() {
		File file = null;

		if (this.chooser.showSaveDialog(this) == JFileChooser.APPROVE_OPTION) {
			try {
				file = this.chooser.getSelectedFile();
				this.textArea.write(new FileWriter(file));
			} catch (IOException e) {
				this.textArea.append("Error: Could not write to file " + file.getName());
			}
		}
	}

	// --------------------------------------------------------------------
}
