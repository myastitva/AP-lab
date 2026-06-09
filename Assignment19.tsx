import { useState } from 'react';
import { View, Text, TouchableOpacity, StyleSheet, SafeAreaView } from 'react-native';

export default function App() {
  const [count, setCount] = useState(0);
  const [isDarkMode, setIsDarkMode] = useState(false);

  const handleIncrement = () => setCount(count + 1);
  const handleDecrement = () => { if (count > 0) setCount(count - 1); };
  const handleReset = () => setCount(0);
  const toggleTheme = () => setIsDarkMode(prev => !prev);

  const theme = isDarkMode ? darkTheme : lightTheme;

  return (
    <View style={[styles.wrapper, { backgroundColor: theme.bg }]}>
      <SafeAreaView style={{ flex: 1 }}>
        <View style={styles.container}>

          {/* Top ticker */}
          <View style={[styles.ticker, { borderColor: theme.neon, backgroundColor: theme.tickerBg }]}>
            <Text style={[styles.tickerText, { color: theme.neon }]}>
              SYS:COUNTER  //  v2.0.1
            </Text>
          </View>

          {/* Big display */}
          <View style={[styles.display, { backgroundColor: theme.displayBg, borderColor: theme.neon, shadowColor: theme.neon }]}>
            {/* Corner accents */}
            <View style={[styles.cornerTL, { borderColor: theme.accent }]} />
            <View style={[styles.cornerBR, { borderColor: theme.accent }]} />

            <Text style={[styles.displayLabel, { color: theme.muted }]}>OUTPUT</Text>
            <Text style={[styles.displayNumber, { color: theme.neon, textShadowColor: theme.neon }]}>
              {String(count).padStart(4, '0')}
            </Text>
            <View style={[styles.scanline, { backgroundColor: theme.neon }]} />
          </View>

          {/* INC / DEC */}
          <View style={styles.row}>
            <TouchableOpacity
              style={[styles.btnSquare, { backgroundColor: theme.decBg, borderColor: theme.decGlow, shadowColor: theme.decGlow }]}
              onPress={handleDecrement}
              activeOpacity={0.6}
            >
              <Text style={[styles.btnSquareSymbol, { color: theme.decGlow }]}>▼</Text>
              <Text style={[styles.btnSquareLabel, { color: theme.decGlow }]}>DEC</Text>
            </TouchableOpacity>

            <TouchableOpacity
              style={[styles.btnSquare, { backgroundColor: theme.incBg, borderColor: theme.incGlow, shadowColor: theme.incGlow }]}
              onPress={handleIncrement}
              activeOpacity={0.6}
            >
              <Text style={[styles.btnSquareSymbol, { color: theme.incGlow }]}>▲</Text>
              <Text style={[styles.btnSquareLabel, { color: theme.incGlow }]}>INC</Text>
            </TouchableOpacity>
          </View>

          {/* Reset */}
          <TouchableOpacity
            style={[styles.btnReset, { backgroundColor: theme.resetBg, borderColor: theme.accent, shadowColor: theme.accent }]}
            onPress={handleReset}
            activeOpacity={0.6}
          >
            <Text style={[styles.btnResetText, { color: theme.accent }]}>[ RESET ]</Text>
          </TouchableOpacity>

          {/* Theme toggle */}
          <TouchableOpacity
            style={[styles.btnMode, { borderColor: theme.muted }]}
            onPress={toggleTheme}
            activeOpacity={0.7}
          >
            <Text style={[styles.btnModeText, { color: theme.muted }]}>
              {isDarkMode ? '◑  LIGHT MODE' : '◐  DARK MODE'}
            </Text>
          </TouchableOpacity>

        </View>
      </SafeAreaView>
    </View>
  );
}

/* ─── Themes ─────────────────────────────────────────────────────── */
const darkTheme = {
  bg:         '#080c14',
  neon:       '#00ffe7',
  accent:     '#ff2d78',
  muted:      '#334455',
  tickerBg:   '#0a1020',
  displayBg:  '#060a10',
  incBg:      '#001a10',
  incGlow:    '#39ff6a',
  decBg:      '#1a0010',
  decGlow:    '#ff3a6e',
  resetBg:    '#10001a',
};

const lightTheme = {
  bg:         '#f0ece3',
  neon:       '#e05c00',
  accent:     '#cc0055',
  muted:      '#b0a898',
  tickerBg:   '#e8e0d0',
  displayBg:  '#faf7f2',
  incBg:      '#e8f5e8',
  incGlow:    '#1a8a3a',
  decBg:      '#f5e8e8',
  decGlow:    '#8a1a1a',
  resetBg:    '#f0e8f5',
};

/* ─── Styles ─────────────────────────────────────────────────────── */
const styles = StyleSheet.create({
  wrapper: { flex: 1 },
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    gap: 14,
    paddingHorizontal: 24,
  },

  /* Ticker */
  ticker: {
    width: '100%',
    borderWidth: 1,
    borderRadius: 4,
    paddingVertical: 6,
    paddingHorizontal: 14,
    marginBottom: 4,
  },
  tickerText: {
    fontSize: 10,
    fontWeight: '700',
    letterSpacing: 2.5,
    fontFamily: 'monospace',
  },

  /* Display */
  display: {
    width: '100%',
    borderWidth: 1.5,
    borderRadius: 8,
    paddingVertical: 36,
    alignItems: 'center',
    shadowOffset: { width: 0, height: 0 },
    shadowOpacity: 0.6,
    shadowRadius: 18,
    elevation: 12,
    overflow: 'hidden',
    marginBottom: 6,
    position: 'relative',
  },
  cornerTL: {
    position: 'absolute',
    top: 8,
    left: 8,
    width: 16,
    height: 16,
    borderTopWidth: 2,
    borderLeftWidth: 2,
  },
  cornerBR: {
    position: 'absolute',
    bottom: 8,
    right: 8,
    width: 16,
    height: 16,
    borderBottomWidth: 2,
    borderRightWidth: 2,
  },
  displayLabel: {
    fontSize: 9,
    fontWeight: '700',
    letterSpacing: 5,
    fontFamily: 'monospace',
    marginBottom: 8,
  },
  displayNumber: {
    fontSize: 80,
    fontWeight: '900',
    fontFamily: 'monospace',
    letterSpacing: 8,
    textShadowOffset: { width: 0, height: 0 },
    textShadowRadius: 16,
  },
  scanline: {
    position: 'absolute',
    bottom: 0,
    left: 0,
    right: 0,
    height: 1,
    opacity: 0.3,
  },

  /* Square buttons */
  row: {
    flexDirection: 'row',
    gap: 12,
    width: '100%',
  },
  btnSquare: {
    flex: 1,
    borderWidth: 1.5,
    borderRadius: 6,
    paddingVertical: 18,
    alignItems: 'center',
    justifyContent: 'center',
    gap: 4,
    shadowOffset: { width: 0, height: 0 },
    shadowOpacity: 0.5,
    shadowRadius: 10,
    elevation: 8,
  },
  btnSquareSymbol: {
    fontSize: 20,
    lineHeight: 24,
  },
  btnSquareLabel: {
    fontSize: 9,
    fontWeight: '700',
    letterSpacing: 4,
    fontFamily: 'monospace',
  },

  /* Reset */
  btnReset: {
    width: '100%',
    borderWidth: 1.5,
    borderRadius: 6,
    paddingVertical: 16,
    alignItems: 'center',
    shadowOffset: { width: 0, height: 0 },
    shadowOpacity: 0.5,
    shadowRadius: 10,
    elevation: 8,
  },
  btnResetText: {
    fontSize: 12,
    fontWeight: '700',
    letterSpacing: 5,
    fontFamily: 'monospace',
  },

  /* Mode toggle */
  btnMode: {
    borderWidth: 1,
    borderRadius: 4,
    paddingVertical: 9,
    paddingHorizontal: 20,
    marginTop: 2,
  },
  btnModeText: {
    fontSize: 10,
    fontWeight: '600',
    letterSpacing: 3,
    fontFamily: 'monospace',
  },
});