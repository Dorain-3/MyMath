import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.lang.reflect.Method;

public class Trigonometric {


	public static void calculate(String s) {
		try {
			Class<?> c = Class.forName("java.lang.Math");
			Method method = c.getDeclaredMethod(s, double.class);
			Object object = c.getDeclaredConstructor().newInstance();


			Double x = 0.0000;
			try {
				String fileName = s + ".txt";
				FileWriter fileWriter = new FileWriter(fileName);
				BufferedWriter bufferedWriter = new BufferedWriter(fileWriter);

				while (x <= 90) {
					Double sin = (Double) method.invoke(object, x);
					;
					String _x = String.format("%5f", x);
					String sin_x = String.format("%5f", sin);
					bufferedWriter.write(_x + " " + sin_x);
					bufferedWriter.newLine();
					x += 0.0001;
				}

				bufferedWriter.close();
				fileWriter.close();
			} catch (IOException e) {
				e.printStackTrace();
			}


		} catch (Exception e) {
			e.printStackTrace();
		}
	}


}

