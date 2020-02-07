package Interview_6_Minute.Original;

import org.junit.Test;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.assertThat;

public class PhoneNumberTest {
  @Test
  public void test1() {

    PhoneNumber ph = new PhoneNumber("+1(858)775-2868");

    assertThat("+1(858)775-2868", is(ph.getOriginalText()));
    assertThat("+18587752868", is(ph.getStrippedNumber()));
    assertThat("(858)775-2868", is(ph.getValueAsNorthAmerican()));
    assertThat("+1.858.775.2868", is(ph.getValueAsInternational()));
  }

  @Test
  public void test2() {
    PhoneNumber ph = new PhoneNumber("+1(858)775-2868x123");

    assertThat("+1(858)775-2868x123", is(ph.getOriginalText()));
    assertThat("+18587752868x123", is(ph.getStrippedNumber()));
    assertThat("(858)775-2868x123", is(ph.getValueAsNorthAmerican()));
    assertThat("+1(858)775-2868x123", is(ph.getValueAsInternational()));
  }

  @Test
  public void test3() {
    PhoneNumber ph = new PhoneNumber("+598.123.4567x858");

    assertThat("+598.123.4567x858", is(ph.getOriginalText()));
    assertThat("+5981234567x858", is(ph.getStrippedNumber()));
    assertThat(null, is(ph.getValueAsNorthAmerican()));
    assertThat("+598.123.456.7x858", is(ph.getValueAsInternational()));
  }

  @Test
  public void test4() {
    PhoneNumber ph = new PhoneNumber("+27 1234 5678 ext 4");

    assertThat("+27 1234 5678 ext 4", is(ph.getOriginalText()));
    assertThat("+2712345678x4", is(ph.getStrippedNumber()));
    assertThat(null, is(ph.getValueAsNorthAmerican()));
    assertThat("+27 1234 5678 ext 4", is(ph.getValueAsInternational()));
  }

  @Test
  public void test5() {
    PhoneNumber ph = new PhoneNumber("858-775-2868");

    assertThat("858-775-2868", is(ph.getOriginalText()));
    assertThat("+18587752868", is(ph.getStrippedNumber()));
    assertThat("(858)775-2868", is(ph.getValueAsNorthAmerican()));
    assertThat("+1.858.775.2868", is(ph.getValueAsInternational()));
  }
}
