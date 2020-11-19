<?php
namespace Kata\Tests\Six_Minute_Interview\_Default;

use PHPUnit\Framework\TestCase;


class FizzBuzz20200810Test extends TestCase
{
    /** @test */
    public function test1()
    {
        $ph = new PhoneNumber("+1(858)775-2868");

        //assertEquals
        $this->assertThat("+1(858)775-2868", $this->equalTo($ph->getOriginalText()));
        $this->assertThat("+18587752868", $this->equalTo($ph->getStrippedNumber()));
        $this->assertThat("(858)775-2868", $this->equalTo($ph->getValueAsNorthAmerican()));
        $this->assertThat("+1.858.775.2868", $this->equalTo($ph->getValueAsInternational()));
    }

    /** @test */
    public function test2()
    {
        $ph = new PhoneNumber("+1(858)775-2868x123");

        $this->assertThat("+1(858)775-2868x123", $this->equalTo($ph->getOriginalText()));
        $this->assertThat("+18587752868x123", $this->equalTo($ph->getStrippedNumber()));
        $this->assertThat("(858)775-2868x123", $this->equalTo($ph->getValueAsNorthAmerican()));
        $this->assertThat("+1(858)775-2868x123", $this->equalTo($ph->getValueAsInternational()));
    }

    /** @test */
    public function test3()
    {
        $ph = new PhoneNumber("+598.123.4567x858");

        $this->assertThat("+598.123.4567x858", $this->equalTo($ph->getOriginalText()));
        $this->assertThat("+5981234567x858", $this->equalTo($ph->getStrippedNumber()));
        $this->assertThat(null, $this->equalTo($ph->getValueAsNorthAmerican()));
        $this->assertThat("+598.123.456.7x858", $this->equalTo($ph->getValueAsInternational()));
    }

    /** @test */
    public function test4()
    {
        $ph = new PhoneNumber("+27 1234 5678 ext 4");

        $this->assertThat("+27 1234 5678 ext 4", $this->equalTo($ph->getOriginalText()));
        $this->assertThat("+2712345678x4", $this->equalTo($ph->getStrippedNumber()));
        $this->assertThat(null, $this->equalTo($ph->getValueAsNorthAmerican()));
        $this->assertThat("+27 1234 5678 ext 4", $this->equalTo($ph->getValueAsInternational()));
    }

    /** @test */
    public function test5()
    {
        $ph = new PhoneNumber("858-775-2868");

        $this->assertEquals("858-775-2868", $ph->getOriginalText());
        $this->assertEquals("+18587752868", $ph->getStrippedNumber());
        $this->assertEquals("(858)775-2868", $ph->getValueAsNorthAmerican());
        $this->assertEquals("+1.858.775.2868", $ph->getValueAsInternational());
    }
}