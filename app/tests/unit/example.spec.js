import { shallowMount } from "@vue/test-utils";
import Test from "@/components/Test.vue";

describe("Test.vue", () => {
  it("renders props.msg when passed", () => {
    const msg = "new message";
    const wrapper = shallowMount(Test, {
      propsData: { msg }
    });
    expect(wrapper.text()).toMatch(msg);
  });
});
