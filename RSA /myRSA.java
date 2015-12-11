/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package rsa;

import java.io.File;
import java.io.FileOutputStream;
import java.io.PrintWriter;
import java.security.KeyPair;
import java.security.KeyPairGenerator;
import java.security.PrivateKey;
import java.security.PublicKey;
import java.security.SecureRandom;
import java.util.Arrays;
import java.util.Scanner;
import javax.crypto.Cipher;

/**
 *
 * @author sr1k4n7h
 */
public class myRSA {
    
    private static SecureRandom sr = new SecureRandom();
    
    public static KeyPair newKeyPair(int rsabits) throws Exception {
        KeyPairGenerator generator = KeyPairGenerator.getInstance("RSA");
        generator.initialize(rsabits, sr);
        return generator.generateKeyPair();
    }
        
    public static byte[] encrypt(byte[] input, PublicKey key) throws Exception {
        Cipher cipher = Cipher.getInstance("RSA/ECB/PKCS1Padding");
        cipher.init(Cipher.ENCRYPT_MODE, key);
        return cipher.doFinal(input);
    }
    
    public static byte[] decrypt(byte[] input, PrivateKey key) throws Exception {
        Cipher cipher = Cipher.getInstance("RSA/ECB/PKCS1Padding");
        cipher.init(Cipher.DECRYPT_MODE, key);
        return cipher.doFinal(input);
    }
    
    public static void main(String[] args) throws Exception {
        
        KeyPair kp = newKeyPair(1<<11);
        PublicKey pubKey = kp.getPublic();
        PrivateKey privKey = kp.getPrivate();
                      
        String plain_text_file = "plain_text.txt";
        String encrypt_text_file = "encrypt_text.txt";
        String decrypt_text_file = "decrypt_text.txt";
        
        String plaintext = "";
        
        Scanner s = new Scanner(new File(plain_text_file));
        
        while(s.hasNextLine()) { plaintext+=s.nextLine(); }
        
        byte[] encrypted_text = encrypt(plaintext.getBytes("UTF-8"),pubKey);
        
        FileOutputStream fos_e = new FileOutputStream(encrypt_text_file);
        fos_e.write(encrypted_text);
        fos_e.close();
        
        System.out.println("Encrypted Text : " + Arrays.toString(encrypted_text));
        System.out.println("Encryption Completed !! Check encrypt_text.txt file ! ");
        
        String decrypted_text = new String(decrypt(encrypted_text,privKey),"UTF-8");
        
        PrintWriter fout = new PrintWriter(decrypt_text_file);
        fout.write(decrypted_text);
        fout.close();
        
        System.out.println("Decrypted Text : " +decrypted_text);
        System.out.println("Decryption Completed !! Check decrypt_text.txt file ! ");
    }
        
}