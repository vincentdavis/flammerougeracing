<template>
  <div>
    <!-- Use the component in the right place of the template -->
    <tiptap-vuetify       v-model="field.value"
 :extensions="extensions" />
  </div>
</template>

<script>
// import the component and the necessary extensions
import {
  TiptapVuetify,
  Heading,
  Bold,
  Italic,
  Strike,
  Underline,
  Code,
  Paragraph,
  BulletList,
  OrderedList,
  ListItem,
  Link,
  Blockquote,
  HardBreak,
  HorizontalRule,
  History,
  TodoList,
  TodoItem,
  Table,
		TableHeader,
		TableCell,
		TableRow,
} from 'tiptap-vuetify'

export default {
  // specify TiptapVuetify component in "components"
  components: { TiptapVuetify },
  props: {
    field: { default: {} }
  },
  data: () => ({
    // declare extensions you want to use
    extensions: [
      History,
      Blockquote,
      Link,
      Underline,
      Strike,
      Italic,
      ListItem,
      BulletList,
      OrderedList,
      [
        Heading,
        {
          options: {
            levels: [1, 2, 3],
          },
        },
      ],
      Bold,
      Code,
      HorizontalRule,
      Paragraph,
      HardBreak,
      TodoList,
      [
        TodoItem,
        {
          options: { nested: true },
        },
      ],
      Table,
		TableHeader,
		TableCell,
		TableRow,
    ],
    
  }),
}
</script>