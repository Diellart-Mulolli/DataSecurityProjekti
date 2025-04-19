#  Projekti: Beaufort Cipher Encoder/Decoder

##  Qëllimi projektit
Ky projekt implementon **algoritmin e shifrimit Beaufort** në Python, duke ofruar:
- Kodim të mesazheve të thjeshta (`Enkriptim`)
- Dekodim të mesazheve të koduar (`Dekriptim`)
- Përpunim të sigurt të tekstit

##  Pjesët Kryesore

### 1. Përpunimi i Tekstit
- **`uppercased(text)`**  
  Shndërron tekstin në shkronja të mëdha  
  *Shembull:* `"Përshëndetje"` → `"PËRSHËNDETJE"`

- **`charrify(text)`**  
  Filtron vetëm shkronjat A-Z (pa shkronja të veçanta)  
  *Shembull:* `"Test123"` → `['T', 'e', 's', 't']`

- **`enumerate_chars(chars)`**  
  Konverton shkronjat në numra (A=0, B=1,...)  
  *Shembull:* `['A','B']` → `[0, 1]`

### 2. Motori i Shifrimit
- **`denumerate(indices)`**  
  Kthen numrat në shkronja  
  *Shembull:* `[0, 1]` → `['A', 'B']`

- **`decharrify(chars)`**  
  Bashkon shkronjat në string  
  *Shembull:* `['A','B']` → `"AB"`

- **`key_resize(key, size)`**  
  Zgjat çelësin për të përputhur gjatësinë e tekstit  
  *Shembull:* `("ÇELËS", 8)` → `"ÇELËSÇEL"`

- **`coded(text, key)`**  
  Aplikon formulën e Beaufort:  
  `(2 * 26 - shkronja_tekstit - shkronja_çelësit - 1) mod 26`

### 3. Ndërfaqja e Përdoruesit
- **Menu kryesore** pranon komanda:
  - `E/e` për enkriptim
  - `D/d` për dekriptim
  - `O/o` për dalje

- **Procesi**:
  1. Përdoruesi vendos tekstin dhe çelësin
  2. Sistemi:
     - Pastron të dhënat
     - Aplikon algoritmin
     - Shfaq rezultatin

## 🔄 Shembull Përdorimi
E/e për Enkriptim | D/d për Dekriptim | O/o për Dalje | Jepni komandën: e
Jepni tekstin: HELLO
Jepni çelësin: KEY
Teksti i Koduar: RIJVS