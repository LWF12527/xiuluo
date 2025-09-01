
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class MainFrame extends JFrame {
    private JTextField inputSizeField;
    private JTextField inputArrayField;
    private JTextField outputHasMainElementField;
    private JTextField outputMainElementField;

    public MainFrame() {
        setTitle("Main Element Finder");
        setSize(300, 200);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);

        // ���������ͱ�ǩ
        JLabel inputSizeLabel = new JLabel("������Ԫ�ظ���:");
        inputSizeField = new JTextField(10);

        JLabel inputArrayLabel = new JLabel("����������:");
        inputArrayField = new JTextField(10);

        JLabel outputHasMainElementLabel = new JLabel("�Ƿ������Ԫ��:");
        outputHasMainElementField = new JTextField(10);
        outputHasMainElementField.setEditable(false);

        JLabel outputMainElementLabel = new JLabel("��Ԫ��:");
        outputMainElementField = new JTextField(10);
        outputMainElementField.setEditable(false);

        // ����ȷ����ť
        JButton confirmButton = new JButton("ȷ��");
        confirmButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // ��ȡ�����Ԫ�ظ���������
                int size = 0;
                try {
                    size = Integer.parseInt(inputSizeField.getText().replaceAll("[^\\d.]", ""));
                } catch (NumberFormatException ex) {
                    // ������Ч������
                    JOptionPane.showMessageDialog(MainFrame.this, "��������Ч��Ԫ�ظ���", "����", JOptionPane.ERROR_MESSAGE);
                    return;
                }

                String arrayString = inputArrayField.getText().trim();

                String[] array = arrayString.split(",");

                // ������������������
                boolean hasMainElement = false;
                int mainElement = 0;
                if (array.length == size) {
                    int[] intArray = new int[size];
                    for (int i = 0; i < size; i++) {
                        try {
                            intArray[i] = Integer.parseInt(array[i].trim());
                        } catch (NumberFormatException ex) {
                            // ������Ч������
                            JOptionPane.showMessageDialog(MainFrame.this, "��������Ч����������", "����", JOptionPane.ERROR_MESSAGE);
                            return;
                        }
                    }
                    // ������������������
                    sortArray(intArray);
                    hasMainElement = checkMainElement(intArray);
                    if (hasMainElement) {
                        mainElement = intArray[size / 2];
                    }
                }

                outputHasMainElementField.setText(String.valueOf(hasMainElement));
                outputMainElementField.setText(String.valueOf(mainElement));
            }
        });


        // ��������
        setLayout(new FlowLayout());

        // �����������
        add(inputSizeLabel);
        add(inputSizeField);
        add(inputArrayLabel);
        add(inputArrayField);
        add(confirmButton);
        add(outputHasMainElementLabel);
        add(outputHasMainElementField);
        add(outputMainElementLabel);
        add(outputMainElementField);
    }

    private void sortArray(int[] array) {
        quickSort(array, 0, array.length - 1);
    }

    private void quickSort(int[] array, int low, int high) {
        if (low < high) {
            int pivotIndex = partition(array, low, high);

            quickSort(array, low, pivotIndex - 1);
            quickSort(array, pivotIndex + 1, high);
        }
    }

    private int partition(int[] array, int low, int high) {
        int pivot = array[high];
        int i = low - 1;

        for (int j = low; j < high; j++) {
            if (array[j] < pivot) {
                i++;
                swap(array, i, j);
            }
        }

        swap(array, i + 1, high);
        return i + 1;
    }

    private void swap(int[] array, int i, int j) {
        int temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }


    private boolean checkMainElement(int[] array) {
        int n = array.length;
        int mid = n / 2;
        if (array[mid] == array[0] || array[mid] == array[n - 1]) {
            return true;
        } else {
            return false;
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                MainFrame frame = new MainFrame();
                frame.setVisible(true);
            }
        });
    }
}
