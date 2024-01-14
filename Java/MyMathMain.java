import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.text.DecimalFormat;

public class MyMathMain {
	public static void main(String[] args) {
		Thread sinThread = new Thread(() -> {
			double x = 0.0000000000000000;
			try {
				String fileName = "sin.txt";
				FileWriter fileWriter = new FileWriter(fileName);
				BufferedWriter bufferedWriter = new BufferedWriter(fileWriter);
				DecimalFormat decimalFormat = new DecimalFormat("#.######");

				while (x <= Math.PI) {
					bufferedWriter.write(decimalFormat.format(x) + " " + decimalFormat.format(StrictMath.sin(x)));
					bufferedWriter.newLine();
					x += 0.000001;
				}
				bufferedWriter.close();
				fileWriter.close();
			} catch (IOException e) {
				e.printStackTrace();
			}
		});
//
//		Thread cosThread = new Thread(() -> {
//			double x = 0.0000000000000000;
//			try {
//				String fileName = "cos.txt";
//				FileWriter fileWriter = new FileWriter(fileName);
//				BufferedWriter bufferedWriter = new BufferedWriter(fileWriter);
//				DecimalFormat decimalFormat = new DecimalFormat("#.######");
//
//				while (x <= Math.PI) {
//					bufferedWriter.write(decimalFormat.format(x) + " " + decimalFormat.format(StrictMath.cos(x)));
//					bufferedWriter.newLine();
//					x += 0.000005;
//				}
//
//				bufferedWriter.close();
//				fileWriter.close();
//			} catch (IOException e) {
//				e.printStackTrace();
//			}
//		});
//
//		Thread tanThread = new Thread(() -> {
//			double x = 0.0000000000000000;
//			try {
//				String fileName = "tan.txt";
//				FileWriter fileWriter = new FileWriter(fileName);
//				BufferedWriter bufferedWriter = new BufferedWriter(fileWriter);
//				DecimalFormat decimalFormat = new DecimalFormat("#.######");
//
//				while (x <= Math.PI) {
//					bufferedWriter.write(decimalFormat.format(x) + " " + decimalFormat.format(StrictMath.tan(x)));
//					bufferedWriter.newLine();
//					x += 0.000005;
//				}
//				bufferedWriter.close();
//				fileWriter.close();
//			} catch (IOException e) {
//				e.printStackTrace();
//			}
//		});


		sinThread.start();
//		cosThread.start();
//		tanThread.start();
	}
}
