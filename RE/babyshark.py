'''
http://www.javadecompilers.com/
- Cây thư mục:
- kctf
    - constants: 
        - Strings.java
            package kctf.constants;

            public class Strings
            {
                public static final String _0xf1a6 = "7P0HJKddEnGG==";
                public static final String _0xflac = "LoE2301mP00FZFWeEQJJR==";
                public static final String _0xface = "N5tFdK18ZKN0442LDVZXSWE7k71Dfr==";
                public static final String _0xfj23 = "ns3PTTDkVYsslUI==";
                public static final String _0xfka6 = "rN88230S8892KL332GDxV1DK=";
                public static final String _0xflag = "S0NURns3SDE1X1dANV8zNDVZX1IxNkg3P30=";
            }
        - Integers.java
            package kctf.constants;

            public class Integers
            {
                public static final int _0x1001 = 99;
                public static final int _0x11 = 23;
                public static final int _0x923 = 0;
                public static final int _0x9901 = 359;
                public static final int _0x19901 = 3359;
                public static final int _0x120 = 923;
                public static final int _0x10001 = 1001;
                public static final int _0x10531 = 786;
                public static final int _0x10 = 99;
                public static final int _0x1 = 99;
                public static final int _0x31 = 99;
                public static final int _0x22 = 99;
                public static final int _0x21 = 99;
            }
    - flag  
        - Flag.java
            package kctf.flag;

            public class Flag
            {
                private static final int count = 0;
                private static final String flag = "KCTF{this_is_not_the_flag}";
                private static final String comment = "You thought this was the flag? LOL";
            }
    - Main.java:
        package kctf;
        public class Main
        {
            public static void main(final String[] args) throws Exception {
                final Sound s = new Sound();
                s.play();
            }
        }
    - Sound.java
        package kctf;

        import javax.sound.sampled.Clip;
        import javax.sound.sampled.AudioInputStream;
        import javax.sound.sampled.AudioSystem;

        public class Sound
        {
            public void play() throws Exception {
                try {
                    final AudioInputStream audioIn = AudioSystem.getAudioInputStream(this.getClass().getClassLoader().getResource("audio.wav").toURI().toURL());
                    final Clip clip = AudioSystem.getClip();
                    clip.open(audioIn);
                    clip.start();
                    while (true) {
                        System.out.println("Baby shark do doo dooo doo");
                    }
                }
                catch (Exception e) {
                    e.printStackTrace();
                }
            }
        }
'''