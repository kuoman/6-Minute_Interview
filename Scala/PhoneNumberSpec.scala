package Interview_6_Minute.Original

import org.scalatest.{FlatSpec, Matchers}

class PhoneNumberSpec extends FlatSpec with Matchers {
  "PhoneNumber" should "test1" in {
    val ph = PhoneNumber("+1(858)775-2868")
    "+1(858)775-2868" should be(ph.originalValue)
    "+18587752868" should be(ph.strippedValue)
    "(858)775-2868" should be(ph.getValueAsNorthAmerican)
    "+1.858.775.2868" should be(ph.getValueAsInternational)
  }

  "PhoneNumber" should "test2" in {
    val ph = PhoneNumber("+1(858)775-2868x123")
    "+1(858)775-2868x123" should be(ph.originalValue)
    "+18587752868x123" should be(ph.strippedValue)
    "(858)775-2868x123" should be(ph.getValueAsNorthAmerican)
    "+1(858)775-2868x123" should be(ph.getValueAsInternational)
  }

  "PhoneNumber" should "test3" in {
    val ph = PhoneNumber("+598.123.4567x858")
    "+598.123.4567x858" should be(ph.originalValue)
    "+5981234567x858" should be(ph.strippedValue)
    "" should be(ph.getValueAsNorthAmerican)
    "+598.123.456.7x858" should be(ph.getValueAsInternational)
  }

  "PhoneNumber" should "test4" in {
    val ph = PhoneNumber("+27 1234 5678 ext 4")
    "+27 1234 5678 ext 4" should be(ph.originalValue)
    "+2712345678x4" should be(ph.strippedValue)
    "" should be(ph.getValueAsNorthAmerican)
    "+27 1234 5678 ext 4" should be(ph.getValueAsInternational)
  }

  "PhoneNumber" should "test5" in {
    val ph = PhoneNumber("858-775-2868")
    "858-775-2868" should be(ph.originalValue)
    "+18587752868" should be(ph.strippedValue)
    "(858)775-2868" should be(ph.getValueAsNorthAmerican)
    "+1.858.775.2868" should be(ph.getValueAsInternational)
  }
}
