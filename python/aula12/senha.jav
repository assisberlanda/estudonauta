import java.util.Scanner;
import java.util.regex.Pattern;

public static Integer validaSenha(String senha) {
	int tamanho = senha.length();
	int x = 0;
	int y;
	boolean senhaMinuscula = Pattern.matches("^(?=.*[a-z]).+$", senha),
			senhaMaiuscula = Pattern.matches("^(?=.*[A-Z]).+$", senha),
			senhaDigito = Pattern.matches("^(?=.*\\d).+$", senha),
			senhaEspecial = Pattern.matches("^(?=.*[-+_!@#$%^&*.,?]).+$", senha);

	if (senhaMinuscula == false) {
		x += 1;
	}
	if (senhaMaiuscula == false) {
		x += 1;
	}
	if (senhaDigito == false) {
		x += 1;
	}
	if (senhaEspecial == false) {
		x += 1;
	}

	if (tamanho + x >= 6) {
		return x;
	} else {
		y = (6 - tamanho);
		return y;
	}

    }
}