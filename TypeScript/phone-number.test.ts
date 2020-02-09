import { PhoneNumber } from "./phone-number";

describe("PhoneNumber Tests", () => {

    it('test1', () => {
        const ph = new PhoneNumber('+1(858)775-2868');

        expect(ph.getOriginalText()).toBe('+1(858)775-2868');
        expect(ph.getStrippedNumber()).toBe('+18587752868');
        expect(ph.getValueAsNorthAmerican()).toBe('(858)775-2868');
        expect(ph.getValueAsInternational()).toBe('+1.858.775.2868');
    });

    it('test2', () => {
        const ph = new PhoneNumber('+1(858)775-2868x123');

        expect(ph.getOriginalText()).toBe('+1(858)775-2868x123');
        expect(ph.getStrippedNumber()).toBe('+18587752868x123');
        expect(ph.getValueAsNorthAmerican()).toBe('(858)775-2868x123');
        expect(ph.getValueAsInternational()).toBe('+1(858)775-2868x123');
    });

    it('test3', () => {
        const ph = new PhoneNumber('+598.123.4567x858');

        expect(ph.getOriginalText()).toBe('+598.123.4567x858');
        expect(ph.getStrippedNumber()).toBe('+5981234567x858');
        expect(ph.getValueAsNorthAmerican()).toBe(null);
        expect(ph.getValueAsInternational()).toBe('+598.123.456.7x858');
    });

    it('test4', () => {
        const ph = new PhoneNumber('+27 1234 5678 ext 4');

        expect(ph.getOriginalText()).toBe('+27 1234 5678 ext 4');
        expect(ph.getStrippedNumber()).toBe('+2712345678x4');
        expect(ph.getValueAsNorthAmerican()).toBe(null);
        expect(ph.getValueAsInternational()).toBe('+27 1234 5678 ext 4');
    });

    it('test5', () => {
        const ph = new PhoneNumber('858-775-2868');

        expect(ph.getOriginalText()).toBe('858-775-2868');
        expect(ph.getStrippedNumber()).toBe('+18587752868');
        expect(ph.getValueAsNorthAmerican()).toBe('(858)775-2868');
        expect(ph.getValueAsInternational()).toBe('+1.858.775.2868');
    });
});